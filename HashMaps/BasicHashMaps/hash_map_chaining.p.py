class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapChaining:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1

# Example usage
if __name__ == "__main__":
    hash_map = HashMapChaining()
    hash_map.put(1, "Apple")
    hash_map.put(11, "Banana")  # Collision will be handled
    print("Value at key 1:", hash_map.get(1))  # Should return Apple
    print("Value at key 11:", hash_map.get(11))  # Should return Banana
