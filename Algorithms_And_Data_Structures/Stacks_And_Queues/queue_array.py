class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)
        return data

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


s = Queue()
print("Initialise queue")
print(f"Is empty? {s.is_empty()}")
print(f"Enque item: {s.enqueue(1)}")
print(f"Enque item: {s.enqueue(2)}")
print(f"Enque item: {s.enqueue(3)}")
print(f"Is empty? {s.is_empty()}")
print(f"Queue size: {s.size_queue()}")
print(f"Peek: {s.peek()}")
print(f"Queue size: {s.size_queue()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Peek: {s.peek()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Queue size: {s.size_queue()}")
print(f"Is empty? {s.is_empty()}")

