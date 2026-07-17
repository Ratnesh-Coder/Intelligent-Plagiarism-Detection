# ============================================================
# LOCALITY SENSITIVE HASHING
# ============================================================

import hashlib

from collections import defaultdict

class LSH:
    def __init__(self, bands=10):
        self.bands = bands
        self.buckets = defaultdict(list)

    def _band_hash(self, band):
        band_str = ",".join(map(str, band))
        return hashlib.md5(band_str.encode()).hexdigest()

    def index(self, doc_name, signature):
        rows = len(signature) // self.bands
        
        for i in range(self.bands):
            start = i * rows
            end = start + rows
            band = signature[start:end]
            bucket_id = (i, self._band_hash(band))
            self.buckets[bucket_id].append(doc_name)

    def query(self, signature):
        candidates = set()
        rows = len(signature) // self.bands
        
        for i in range(self.bands):
            start = i * rows
            end = start + rows
            band = signature[start:end]
            bucket_id = (i, self._band_hash(band))
            
            for doc in self.buckets.get(bucket_id, []):
                candidates.add(doc)

        return candidates