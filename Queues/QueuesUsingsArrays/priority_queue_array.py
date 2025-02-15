import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
        print(f"Enqueued: {item} with priority {priority}")

    def dequeue(self):
        if self.is_empty():
            print("Priority Queue is empty!")
            return None
        removed = heapq.heappop(self.queue)
        print(f"Dequeued: {removed[1]} with priority {removed[0]}")
        return removed[1]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Priority Queue:", self.queue)


# Example usage
if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue("Task A", 2)
    pq.enqueue("Task B", 1)
    pq.enqueue("Task C", 3)
    pq.display()
    pq.dequeue()
    pq.display()
