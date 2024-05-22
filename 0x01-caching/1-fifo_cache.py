#!/usr/bin/env python3
"""
1-fifo_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching using a dictionary
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

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
