class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, item):
        if not self.stack:
            self.max_stack.append(item)
        elif item > self.max_stack[-1]:
            self.max_stack.append(item)
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

            if data == self.max_stack[-1]:
                del self.max_stack[-1]

            return data

    def is_empty(self):
        return len(self.stack) == 0

    def stack_size(self):
        return len(self.stack)

    def max_in_stack(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


s = Stack()
print("Initialise stack")
print(f"Is empty? {s.is_empty()}")
print(f"Push item: {s.push(1)}")
print(f"Push item: {s.push(2)}")
print(f"Push item: {s.push(42)}")
print(f"Push item: {s.push(69)}")
print(f"Push item: {s.push(3)}")
print(f"Max in stack: {s.max_in_stack()}")
print(f"Is empty? {s.is_empty()}")
print(f"Stack size: {s.stack_size()}")
print(f"Peek: {s.peek()}")
print(f"Stack size: {s.stack_size()}")
print(f"Pop item: {s.pop()}")
print(f"Pop item: {s.pop()}")
print(f"Max in stack: {s.max_in_stack()}")
print(f"Pop item: {s.pop()}")
print(f"Pop item: {s.pop()}")
print(f"Pop item: {s.pop()}")
print(f"Pop item: {s.pop()}")
print(f"Stack size: {s.stack_size()}")
print(f"Is empty? {s.is_empty()}")
print(f"Max in stack: {s.max_in_stack()}")
