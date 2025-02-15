from collections import deque

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.queue = deque()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.queue.remove(key)
            self.queue.append(key)  # Move to end (recently used)
            return self.cache[key]
        return -1  # Not found

    def put(self, key, value):
        if key in self.cache:
            self.queue.remove(key)
        elif len(self.cache) >= self.capacity:
            lru_key = self.queue.popleft()
            del self.cache[lru_key]
        self.queue.append(key)
        self.cache[key] = value

    def display(self):
        print("LRU Cache State:", {key: self.cache[key] for key in self.queue})

# Example usage
if __name__ == "__main__":
    lru = LRUCache(3)
    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    lru.display()
    lru.get(2)
    lru.put(4, "D")  # Evicts least recently used (1)
    lru.display()
