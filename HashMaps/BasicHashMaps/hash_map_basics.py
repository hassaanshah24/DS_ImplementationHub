class MyHashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def put(self, key, value):
        index = key % self.size
        self.map[index] = value

    def get(self, key):
        index = key % self.size
        return self.map[index] if self.map[index] is not None else -1

    def remove(self, key):
        index = key % self.size
        self.map[index] = None

# Example usage
if __name__ == "__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 100)
    myHashMap.put(2, 200)
    print("Value at key 1:", myHashMap.get(1))  # Should return 100
    myHashMap.remove(1)
    print("Value at key 1 after removal:", myHashMap.get(1))  # Should return -1
