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

    def reverse(self):
        if self.head is None:
            return

        current_node = self.head
        new_node = current_node.next_node
        current_node.next_node = None

        while current_node is not None and new_node is not None:
            p = new_node.next_node
            q = new_node    
            new_node.next_node = current_node
            new_node = p
            current_node = q

        self.head = current_node

        


        


if __name__ == "__main__":
    l = LinkedList()
    l.insert_start(5)
    l.insert_start(1)
    l.insert_end(6)
    l.insert_start(0)
    l.insert_end(10)
    l.insert_end(100)
    l.insert_start(69)
    l.remove(6)
    l.remove(10)
    l.remove(0)
    l.remove(42)
    l.size_of_list()
    l.traverse()
    print()
    l.reverse()
    l.traverse()
