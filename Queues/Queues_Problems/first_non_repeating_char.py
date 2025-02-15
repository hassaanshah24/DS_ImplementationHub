from collections import deque, Counter


class FirstNonRepeating:
    def __init__(self):
        self.queue = deque()
        self.freq = Counter()

    def add_character(self, char):
        self.freq[char] += 1
        if self.freq[char] == 1:
            self.queue.append(char)

        # Remove repeating characters from the front
        while self.queue and self.freq[self.queue[0]] > 1:
            self.queue.popleft()

        # Return the first non-repeating character
        return self.queue[0] if self.queue else None


# Example usage
if __name__ == "__main__":
    stream = "aabcddbe"
    fnr = FirstNonRepeating()
    print("Stream:", stream)
    print("First Non-Repeating Character at each step:")
    for ch in stream:
        print(f"After adding '{ch}': {fnr.add_character()}")
