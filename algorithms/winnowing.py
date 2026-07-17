# ============================================================
# WINNOWING FINGERPRINTING ALGORITHM
# ============================================================

import hashlib

def hash_kgram(kgram):
    """
    Hash a k-gram using SHA1 and convert to integer
    """

    return int(hashlib.sha1(kgram.encode()).hexdigest(), 16)

def generate_kgrams(text, k=3):
    """
    Generate k-grams from text
    """

    tokens = text.split()

    kgrams = []

    for i in range(len(tokens) - k + 1):

        kgram = " ".join(tokens[i:i+k])

        kgrams.append(kgram)

    return kgrams


def winnowing(text, k=3, window_size=5):
    """
    Generate document fingerprints using Winnowing algorithm
    """

    kgrams = generate_kgrams(text, k)

    hashes = [hash_kgram(kgram) for kgram in kgrams]

    fingerprints = set()

    if len(hashes) < window_size:
        return set(hashes)

    for i in range(len(hashes) - window_size + 1):

        window = hashes[i:i+window_size]

        min_hash = min(window)

        fingerprints.add(min_hash)

    return fingerprints


def fingerprint_similarity(fp1, fp2):
    """
    Compute similarity between two fingerprint sets
    """

    if not fp1 or not fp2:
        return 0

    intersection = len(fp1.intersection(fp2))
    union = len(fp1.union(fp2))

    return intersection / union