#!/usr/bin/env python3
"""
3-lru_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Basic caching using a dictionary
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
            lru_key = self.order.pop(0)
            print(f"DISCARD: {lru_key}")
            del self.cache_data[lru_key]

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
