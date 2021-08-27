class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return item

    def peek(self):
        if not self.is_empty:
            return None
        return self.stack[-1]

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            data = self.stack[-1]
            del self.stack[-1]
            return data

    def is_empty(self):
        return len(self.stack) == 0

    def stack_size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack() 

    def is_empty(self):
        return self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty()

    def flip_stacks(self, stack1, stack2):
        if stack1.is_empty():
            return
        stack2.push(stack1.pop())
        self.flip_stacks(stack1, stack2)

    def enqueue(self, data):
        self.enqueue_stack.push(data)
        return data

    def dequeue(self):
        self.flip_stacks(self.enqueue_stack, self.dequeue_stack)
        return self.dequeue_stack.pop()

    def peek(self):
        if self.enqueue_stack.is_empty() and self.dequeue_stack.is_empty():
            return None
        elif not self.dequeue_stack.is_empty():
            return self.dequeue_stack.peek()
        else:
            self.flip_stacks(self.enqueue_stack, self.dequeue_stack)
            return self.dequeue_stack.peek()
            

    def size_queue(self):
        return self.enqueue_stack.stack_size() + self.dequeue_stack.stack_size()


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
print(f"Enque item: {s.enqueue(1)}")
print(f"Enque item: {s.enqueue(2)}")
print(f"Enque item: {s.enqueue(3)}")
print(f"Is empty? {s.is_empty()}")
print(f"Queue size: {s.size_queue()}")
print(f"Peek: {s.peek()}")
print(f"Queue size: {s.size_queue()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Peek: {s.peek()}")
print(f"Enque item: {s.enqueue(99)}")
print(f"Peek: {s.peek()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Enque item: {s.enqueue(1)}")
print(f"Enque item: {s.enqueue(50)}")
print(f"Dequeue item: {s.dequeue()}")
print(f"Queue size: {s.size_queue()}")
print(f"Is empty? {s.is_empty()}")
