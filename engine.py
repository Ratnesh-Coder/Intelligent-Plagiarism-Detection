# ============================================================
# PLAGIARISM DETECTION ENGINE
# ============================================================

import nltk
from concurrent.futures import ThreadPoolExecutor

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess_text
from similarity import jaccard_similarity, minhash_signature, minhash_similarity

from algorithms.kmp import kmp_search
from algorithms.rabin_karp import rabin_karp_search
from algorithms.winnowing import winnowing, fingerprint_similarity

from indexer import load_index, build_index
from report import generate_html_report


# Load semantic model once
model = SentenceTransformer('all-MiniLM-L6-v2')


# ============================================================
# DOCUMENT PROCESSING WORKER
# ============================================================

def process_document(filename, data, query_doc, query_sentences,
                     query_embeddings, query_signature,
                     query_fingerprint):

    doc = data["text"]
    doc_signature = data["minhash"]
    doc_fingerprint = data["fingerprint"]

    mh_similarity = minhash_similarity(query_signature, doc_signature)

    fp_similarity = fingerprint_similarity(query_fingerprint, doc_fingerprint)

    if mh_similarity < 0.05 and fp_similarity < 0.05:
        mh_similarity = 0
        fp_similarity = 0

    ngram_score = jaccard_similarity(query_doc, doc)

    sentences = nltk.sent_tokenize(doc)
    
    if not sentences:
        sentences = [doc]

    embeddings = model.encode(sentences)

    similarities = cosine_similarity(query_embeddings, embeddings)

    plagiarized = 0
    matches = []

    for i in range(len(query_sentences)):

        max_similarity = similarities[i].max()
        best_index = similarities[i].argmax()
        best_sentence = sentences[best_index]

        if max_similarity > 0.4:

            plagiarized += 1

            matches.append({
                "query": query_sentences[i],
                "source": best_sentence,
                "score": max_similarity
            })

    semantic_score = plagiarized / max(len(query_sentences), 1)

    final_score = (
        0.40 * semantic_score +
        0.25 * ngram_score +
        0.20 * fp_similarity +
        0.15 * mh_similarity
    ) * 100

    return (filename, final_score, ngram_score, doc, matches)


# ============================================================
# MAIN PLAGIARISM SEARCH
# ============================================================

def plagiarism_search(query_doc):

    data = load_index()

    if data is None:
        build_index()
        data = load_index()

    index = data["documents"]
    lsh = data["lsh"]

    # --------------------------------------------------------
    # QUERY PREPARATION
    # --------------------------------------------------------

    query_doc = preprocess_text(query_doc)

    query_sentences = nltk.sent_tokenize(query_doc)
    
    if not query_sentences:
        query_sentences = [query_doc]

    query_embeddings = model.encode(query_sentences)

    query_signature = minhash_signature(query_doc)

    query_fingerprint = winnowing(query_doc)

    candidates = lsh.query(query_signature)
    
    if not candidates:
        candidates = index.keys()

    results = []
    all_matches = []

    # --------------------------------------------------------
    # PARALLEL DOCUMENT PROCESSING
    # --------------------------------------------------------

    with ThreadPoolExecutor() as executor:

        futures = []

        for filename in candidates:

            data = index[filename]

            futures.append(

                executor.submit(
                    process_document,
                    filename,
                    data,
                    query_doc,
                    query_sentences,
                    query_embeddings,
                    query_signature,
                    query_fingerprint
                )

            )

        for future in futures:

            result = future.result()

            if result:

                filename, score, ngram_score, doc, matches = result

                results.append((filename, score, ngram_score, doc))

                all_matches.extend(matches)

    # --------------------------------------------------------
    # SORT RESULTS
    # --------------------------------------------------------

    results.sort(key=lambda x: x[1], reverse=True)

    generate_html_report(results, all_matches)

    # --------------------------------------------------------
    # TEXT REPORT
    # --------------------------------------------------------

    report = "Plagiarism Results\n\n"

    for r in results:

        report += f"{r[0]} → {round(r[1],2)}% (N-gram {round(r[2],2)})\n"

    # --------------------------------------------------------
    # EXACT MATCH ANALYSIS
    # --------------------------------------------------------

    if results:

        best_doc = results[0]

        pattern = query_sentences[0]

        kmp_matches = kmp_search(pattern, best_doc[3])

        rk_matches = rabin_karp_search(pattern, best_doc[3])

        report += "\nExact Pattern Matches\n"

        report += f"KMP Positions: {kmp_matches}\n"

        report += f"Rabin-Karp Positions: {rk_matches}\n"

    return report