#!/usr/bin/env python3
"""
4-mru_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRU caching using a dictionary.
    Most Recently Used.
    """

    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            print(f"DISCARD: {mru_key}")
            del self.cache_data[mru_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key, None)
