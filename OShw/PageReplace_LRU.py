class LRUCache:

    def __init__(self, capacity):
        self.cache = {}
        self.used_list = []
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            if key != self.used_list[-1]:
                self.used_list.remove(key)
                self.used_list.append(key)
            return self.cache[key]
        else:
            return -1
        
        
    def set(self, key, value):
        if key in self.cache:
            self.used_list.remove(key)
        elif len(self.cache) == self.capacity:
            self.cache.pop(self.used_list.pop(0))
        self.used_list.append(key)
        self.cache[key] = value
        print(self.used_list)

    def __str__(self):
        return self.cache

if __name__ == "__main__":
    lru = LRUCache(3)
    lru.set(7,7)
    lru.set(0,0)
    lru.set(1,2)
    lru.set(2,1)
    lru.set(0,1)
    lru.set(3,5)
    lru.set(0,1)
    
    
