class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item, priority):
        new_node = Node(item, priority)
        if self.is_empty() or self.front.priority > priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front
            while temp.next and temp.next.priority <= priority:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue is empty!")
            return None
        removed = self.front.data
        self.front = self.front.next
        print(f"Dequeued: {removed}")
        return removed

    def display(self):
        temp = self.front
        print("Priority Queue:", end=" ")
        while temp:
            print(f"[{temp.data}, P{temp.priority}]", end=" -> ")
            temp = temp.next
        print("None")


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", 2)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 3)
    pq.display()
    pq.dequeue()
    pq.display()
