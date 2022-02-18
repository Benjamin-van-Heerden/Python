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

    def size_of_list(self):
        print(f"Size: {self.num_of_nodes}")

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None


        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.previous

        if actual_node is None:
            print(f"{data} not found!")
            return
        
        self.num_of_nodes -= 1
        if previous_node is None:
            self.head = actual_node.previous
        else:
            previous_node.previous = actual_node.previous
        print(f"Removed {actual_node.data}")
        return

        


if __name__ == "__main__":
    l = DoublyLinkedList()
    l.insert_start(5)
    l.insert_start(1)
    l.insert_end(6)
    l.insert_start(0)
    l.insert_end(10)
    l.insert_end(11)
    l.remove(6)
    l.remove(10)
    l.remove(0)
    l.remove(42)
    l.size_of_list()
    l.traverse()
