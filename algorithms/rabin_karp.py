# ============================================================
# RABIN-KARP STRING MATCHING ALGORITHM
# ============================================================

def rabin_karp_search(pattern, text, prime=101):
    
    if not pattern or not text:
        return []

    if len(pattern) > len(text):
        return []

    d = 256

    m = len(pattern)
    n = len(text)

    p_hash = 0
    t_hash = 0
    h = 1

    results = []

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):

        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for i in range(n - m + 1):

        if p_hash == t_hash:

            if text[i:i+m] == pattern:
                results.append(i)

        if i < n - m:

            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i+m])) % prime

            if t_hash < 0:
                t_hash += prime

    return results