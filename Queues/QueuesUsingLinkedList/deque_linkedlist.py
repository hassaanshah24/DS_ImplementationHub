class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def insert_front(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        print(f"Inserted at front: {item}")

    def insert_rear(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        print(f"Inserted at rear: {item}")

    def delete_front(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        removed = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        print(f"Deleted from front: {removed}")
        return removed

    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty!")
            return None
        removed = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        print(f"Deleted from rear: {removed}")
        return removed

    def display(self):
        if self.is_empty():
            print("Deque is empty!")
            return
        temp = self.front
        print("Deque:", end=" ")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    dq = Deque()
    dq.insert_rear(10)
    dq.insert_rear(20)
    dq.insert_front(5)
    dq.display()
    dq.delete_front()
    dq.delete_rear()
    dq.display()
