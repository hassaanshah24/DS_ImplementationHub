class Queue:
    def __init__(self, size=10):
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return self.rear == self.size - 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1  # Reset queue when empty
        else:
            self.front += 1
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        return None if self.is_empty() else self.queue[self.front]

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            print("Queue:", self.queue[self.front:self.rear+1])


# Example usage
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
