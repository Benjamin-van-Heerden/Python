class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def size_of_list(self):
        print(f"Size: {self.num_of_nodes}")

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None


        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node 

        if actual_node is None:
            print(f"{data} not found!")
            return
        
        self.num_of_nodes -= 1
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node
        print(f"Removed {actual_node.data}")
        return

    def middle_node(self):
        middle_index = self.num_of_nodes//2

        actual_node = self.head
        for i in range(middle_index):
            actual_node = actual_node.next_node

        print(f"Middle node is {actual_node.data}")

    def middle_fast_slow(self):

        slow = self.head
        fast = self.head

        while fast.next_node and fast.next_node.next_node:
            fast = fast.next_node.next_node
            slow = slow.next_node

        print(f"Middle node is {slow.data}")




if __name__ == "__main__":
    l = LinkedList()
    l.insert_start(5)
    l.insert_start(1)
    l.insert_end(6)
    l.insert_start(0)
    l.insert_end(10)
    l.remove(6)
    l.remove(10)
    l.remove(42)
    l.size_of_list()
    l.traverse()
    l.middle_node()
    l.middle_fast_slow()
