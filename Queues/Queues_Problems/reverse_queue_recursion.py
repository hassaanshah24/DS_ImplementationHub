from collections import deque


class QueueReverser:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None

    def reverse(self):
        if not self.queue:
            return
        front = self.dequeue()
        self.reverse()
        self.enqueue(front)

    def display(self):
        print("Queue:", list(self.queue))


# Example usage
if __name__ == "__main__":
    qr = QueueReverser()
    qr.enqueue(10)
    qr.enqueue(20)
    qr.enqueue(30)
    qr.enqueue(40)

    print("Original Queue:")
    qr.display()

    qr.reverse()

    print("Reversed Queue:")
    qr.display()
