from collections import deque

class lru_cache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.q = deque()

    def get(self, key):
        if key in self.dic:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.dic[key]
        return -1

    def set(self, key, value):
        if key in self.dic:
            self.q.remove(key)
        elif self.capacity == len(self.dic):
            key_to_remove = self.q.pop()
            del self.dic[key_to_remove]
            self.q.appendleft(key)
            self.dic[key] = value