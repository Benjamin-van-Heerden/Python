class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.num_of_items = 0

    def insert(self, data):
        self.num_of_items += 1
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # visit left subtree
        if data < node.data:
            if node.left_child is not None:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # visit right subtree
        else:
            if node.right_child is not None:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def traverse(self):
        self.ordered = []
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child is not None:
            self.traverse_in_order(node.left_child)

        self.ordered.append(node.data)

        if node.right_child is not None:
            self.traverse_in_order(node.right_child)

    def get_max(self):
        if self.root is not None:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_child is not None:
            return self.get_max_value(node.right_child)
        else:
            return node.data

    def get_min(self):
        if self.root is not None:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_child is not None:
            return self.get_min_value(node.left_child)
        else:
            return node.data

    def remove_node(self, data, node="root"):
        if node == "root":
            node = self.root

        if node is None:
            return

        # first we must search for the given node
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            self.num_of_items -= 1
            # 4 cases:
            # the node is a leaf node
            if node.left_child is None and node.right_child is None:
                print(f"Removing a leaf node with value {node.data}")

                parent = node.parent
                if parent is not None and parent.left_child == node:
                    parent.left_child = None
                if parent is not None and parent.right_child == node:
                    parent.right_child = None
                if parent is None:
                    self.root = None

                del node
            # the node has a single right child
            elif node.left_child is None and node.right_child is not None:
                print(
                    f"Removing node with single right child, value {node.data}")

                parent = node.parent
                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.right_child
                    if parent.right_child == node:
                        parent.right_child = node.right_child
                else:
                    self.root = node.right_child

                del node
            # the node has a single left child
            elif node.left_child is not None and node.right_child is None:
                print(
                    f"Removing node with single left child, value {node.data}")

                parent = node.parent
                if parent is not None:
                    if parent.left_child == node:
                        parent.left_child = node.left_child
                    if parent.right_child == node:
                        parent.right_child = node.left_child
                else:
                    self.root = node.left_child

                del node
            # the node has two children
            else:
                print(f"Removing node with two children, value: {node.data}")

                predecessor = self.get_predecessor(node.left_child)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)

    def get_predecessor(self, node):
        # the predecessor is the max value in the left subtree
        if node.right_child is not None:
            return self.get_predecessor(node.right_child)
        else:
            return node


def tree_equal(tree1, tree2):
    if tree1.num_of_items != tree2.num_of_items:
        return False
    # both trees are traversed simultaneously, the operations being dictated by tree1
    # if any discrepancies are found we return False otherwise if the trees have been traversed
    # with no discrepancies we return True.

    node1 = tree1.root
    node2 = tree2.root

    return nodes_traverse_equal(node1, node2)


def nodes_traverse_equal(node1, node2):
    # since node1 will never be None we return false if node2 is None
    if node2 is None:
        return False
    elif node1.data != node2.data:
        return False
    else:
        if node1.left_child is not None:
            return nodes_traverse_equal(node1.left_child, node2.left_child)
        
        if node2.right_child is not None:
            return nodes_traverse_equal(node1.right_child, node2.right_child)

    # if all has been checked return True
    return True


bst1 = BinarySearchTree()
bst1.insert(5)
bst1.insert(12)
# bst1.insert(42)
# bst1.insert(1)
# bst1.insert(-10)
# bst1.insert(11)
# bst1.insert(4)
# bst1.insert(-100)

bst2 = BinarySearchTree()
bst2.insert(5)
bst2.insert(12)
# bst2.insert(42)
# bst2.insert(1)
# bst2.insert(-10)
# bst2.insert(11)
# bst2.insert(4)
# bst2.insert(-100)

bst3 = BinarySearchTree()
# bst3.insert(5)
bst3.insert(12)
bst3.insert(42)
bst3.insert(1)
bst3.insert(-10)
bst3.insert(11)
bst3.insert(4)

bst4 = BinarySearchTree()
bst4.insert(4)
bst4.insert(2)
bst4.insert(1)
bst4.insert(42)
bst4.insert(-100)


print(tree_equal(bst1, bst2))
print(tree_equal(bst2, bst3))
print(tree_equal(bst1, bst4))
