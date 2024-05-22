#!/usr/bin/env python3
"""
0-basic_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic caching using a dictionary
    """

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
