#!/usr/bin/env python3
"""
2-lifo_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
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
            last_key = self.order.pop()
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
