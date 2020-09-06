# 9-5-2020
# https://leetcode.com/problems/lru-cache/

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.set_lru(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.set_lru(key)
        if len(self.cache) == self.capacity and key not in self.cache:
            del self.cache[self.lru.pop(0)]
        self.cache[key] = value
    
    def set_lru(self, key: int):
        if key in self.lru:
            self.lru.remove(key)
        self.lru.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
