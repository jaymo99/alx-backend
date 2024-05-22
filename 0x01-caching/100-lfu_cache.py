#!/usr/bin/env python3
"""
100-lfu_cache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU caching using a dictionary.
    Least Frequently Used.
    """

    def __init__(self):
        """Class constructor"""
        super().__init__()
        self.frequency = {}
        self.order = []

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]

                if len(lfu_keys) > 1:
                    for k in self.order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                self.order.remove(lfu_key)

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order.append(key)

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data.get(key, None)
