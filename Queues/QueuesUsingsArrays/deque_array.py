class Deque:
    def __init__(self, size=5):
        self.deque = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def insert_front(self, item):
        if self.is_full():
            print("Deque is full!")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = item
        print(f"Inserted at front: {item}")

    def insert_rear(self, item):
        if self.is_full():
            print("Deque is full!")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = item
        print(f"Inserted at rear: {item}")

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        removed = self.deque[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Deleted from front: {removed}")
        return removed

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        removed = self.deque[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        print(f"Deleted from rear: {removed}")
        return removed

    def display(self):
        if self.is_empty():
            print("Deque is empty!")
            return
        index = self.front
        print("Deque:", end=" ")
        while True:
            print(self.deque[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()


# Example usage
if __name__ == "__main__":
    dq = Deque(5)
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.display()
    dq.delete_front()
    dq.delete_rear()
    dq.display()
