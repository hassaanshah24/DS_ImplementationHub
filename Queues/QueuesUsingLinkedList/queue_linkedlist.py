class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Reset queue when empty
        print(f"Dequeued: {removed}")
        return removed

    def peek(self):
        return None if self.is_empty() else self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            temp = self.front
            print("Queue:", end=" ")
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")


# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    q.dequeue()
    q.display()
