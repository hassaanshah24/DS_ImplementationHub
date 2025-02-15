from collections import deque


class QueueInterleaver:
    def __init__(self, queue):
        self.queue = deque(queue)

    def interleave(self):
        size = len(self.queue)
        if size % 2 != 0:
            print("Queue must have an even number of elements!")
            return
        first_half = deque()

        for _ in range(size // 2):
            first_half.append(self.queue.popleft())

        while first_half:
            self.queue.append(first_half.popleft())
            self.queue.append(self.queue.popleft())

    def display(self):
        print("Interleaved Queue:", list(self.queue))


# Example usage
if __name__ == "__main__":
    q = QueueInterleaver([1, 2, 3, 4, 5, 6, 7, 8])
    print("Original Queue:", q.queue)
    q.interleave()
    q.display()
