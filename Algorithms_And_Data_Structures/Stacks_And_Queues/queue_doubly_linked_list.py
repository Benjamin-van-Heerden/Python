class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0
        self.tail = None

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.head
            self.head.next = new_node
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail
            self.tail.previous = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return
        self.num_of_nodes -= 1
        self.head = self.head.previous

    def length(self):
        return self.num_of_nodes


class Queue:
    def __init__(self):
        self.queue = DoublyLinkedList()

    def is_empty(self):
        return self.queue.length() == 0
    
    def enqueue(self, data):
        self.queue.insert_end(data)
        return data

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.queue.head.data
        self.queue.remove_head()
        return data

    def peek(self):
        if self.is_empty():
            return None
        return self.queue.head.data

    def size_queue(self):
        return self.queue.length()


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