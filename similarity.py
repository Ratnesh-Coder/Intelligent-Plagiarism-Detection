# ==========================================================
# SIMILARITY ALGORITHMS MODULE
# ==========================================================

import nltk
import random
import hashlib

# ============================================================
# N-GRAM GENERATION
# ============================================================

def generate_ngrams(text, n=2):

    tokens = nltk.word_tokenize(text.lower())

    grams = []

    for i in range(len(tokens) - n + 1):
        grams.append(" ".join(tokens[i:i+n]))

    return grams

# ==========================================================
# JACCARD SIMILARITY
# ==========================================================

def jaccard_similarity(text1, text2):

    ngrams1 = set(generate_ngrams(text1))
    ngrams2 = set(generate_ngrams(text2))

    union = ngrams1.union(ngrams2)

    if len(union) == 0:
        return 0

    intersection = ngrams1.intersection(ngrams2)

    return len(intersection) / len(union)


# ============================================================
# MINHASH SIGNATURE
# ============================================================

def minhash_signature(text, num_hashes=50):

    random.seed(42)

    tokens = set(generate_ngrams(text))

    if not tokens:
        return [0] * num_hashes

    signatures = []

    max_hash = 2**32 - 1

    for _ in range(num_hashes):

        a = random.randint(1, max_hash)
        b = random.randint(0, max_hash)

        min_hash = min(
            (a * int(hashlib.md5(t.encode()).hexdigest(), 16) + b) % max_hash
            for t in tokens
        )

        signatures.append(min_hash)

    return signatures

# ==========================================================
# MINHASH SIMILARITY
# ==========================================================

def minhash_similarity(sig1, sig2):

    matches = sum(1 for a, b in zip(sig1, sig2) if a == b)

    return matches / len(sig1)