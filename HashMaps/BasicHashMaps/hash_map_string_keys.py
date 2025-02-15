class StringHashMap:
    def __init__(self):
        self.size = 10000
        self.map = [None] * self.size

    def calculate_hash_value(self, string):
        return ord(string[0]) * 100 + ord(string[1])

    def put(self, string):
        hash_code = self.calculate_hash_value(string)
        if self.map[hash_code]:
            self.map[hash_code].append(string)
        else:
            self.map[hash_code] = [string]

    def get(self, string):
        hash_code = self.calculate_hash_value(string)
        if self.map[hash_code] and string in self.map[hash_code]:
            return hash_code
        return -1

# Example usage
if __name__ == "__main__":
    hash_table = StringHashMap()
    hash_table.put("UDOMETER")
    print("Hash Value of 'UDOMETER':", hash_table.get("UDOMETER"))  # Should return hash value
