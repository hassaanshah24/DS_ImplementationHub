class HashMapOpenAddressing:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key, i):
        return (key + i) % self.size

    def put(self, key, value):
        for i in range(self.size):
            index = self.hash_function(key, i)
            if self.table[index] is None:
                self.table[index] = (key, value)
                return
        print("Hash table full!")

    def get(self, key):
        for i in range(self.size):
            index = self.hash_function(key, i)
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]
        return -1

# Example usage
if __name__ == "__main__":
    hash_map = HashMapOpenAddressing()
    hash_map.put(5, "Orange")
    hash_map.put(15, "Mango")  # Collision will be resolved
    print("Value at key 5:", hash_map.get(5))  # Should return Orange
