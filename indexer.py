# ============================================================
# DOCUMENT INDEXING MODULE
# ============================================================

import os
import pickle

from document_reader import read_document
from preprocessing import preprocess_text
from similarity import minhash_signature
from algorithms.winnowing import winnowing
from lsh import LSH

INDEX_FILE = "document_index.pkl"


def build_index(folder="documents"):
    """
    Build fingerprint index for all documents
    """

    index = {}
    lsh = LSH()

    for filename in os.listdir(folder):
        
        if not filename.endswith((".txt", ".pdf", ".docx")):
            continue

        path = os.path.join(folder, filename)

        try:

            doc = read_document(path)

            doc = preprocess_text(doc)

            signature = minhash_signature(doc)

            index[filename] = {
                "text": doc,
                "minhash": signature,
                "fingerprint": winnowing(doc)
            }

            lsh.index(filename, signature)

        except Exception:
            continue


    index_data = {
        "documents": index,
        "lsh": lsh
    }

    with open(INDEX_FILE, "wb") as f:
        pickle.dump(index_data, f)

    print("Document index built successfully.")


def load_index():
    """
    Load document index
    """

    if not os.path.exists(INDEX_FILE):
        return None

    with open(INDEX_FILE, "rb") as f:
        return pickle.load(f)