class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.rear = new_node
            self.rear.next = new_node  # Circular link
        else:
            new_node.next = self.rear.next
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        front = self.rear.next
        removed = front.data
        if self.rear == front:  # Only one node
            self.rear = None
        else:
            self.rear.next = front.next
        print(f"Dequeued: {removed}")
        return removed

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        temp = self.rear.next
        print("Circular Queue:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.rear.next:
                break
        print("(Back to front)")


# Example usage
if __name__ == "__main__":
    cq = CircularQueue()
    cq.enqueue(10)
    cq.enqueue(20)
    cq.enqueue(30)
    cq.display()
    cq.dequeue()
    cq.display()
