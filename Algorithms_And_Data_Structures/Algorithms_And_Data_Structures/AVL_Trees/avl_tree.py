class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVLTree:
    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def remove(self, data):
        if self.root is not None:
            self.remove_node(data, self.root)
        print(f"New root: {self.root.data}")

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
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
                # after deletion we have to check if the AVL properties are violated
                self.handle_violation(parent)
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

                node.right_child.parent = parent
                del node
                # after deletion we have to check if the AVL properties are violated
                self.handle_violation(parent)
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

                node.left_child.parent = parent
                del node
                # after deletion we have to check if the AVL properties are violated
                self.handle_violation(parent)
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

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
        print(f"New root: {self.root.data}")

    def insert_node(self, data, node):
        if data < node.data:
            if node.left_child is not None:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
                node.height = max(self.calc_height(
                    node.left_child), self.calc_height(node.right_child)) + 1
        else:
            if node.right_child is not None:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)
                node.height = max(self.calc_height(
                    node.left_child), self.calc_height(node.right_child)) + 1
        # after every insertion we have to check if the AVL properties are violated
        self.handle_violation(node)

    def calc_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def calculate_balance(self, node):
        if node is None:
            return 0
        else:
            return self.calc_height(node.left_child) - self.calc_height(node.right_child)

    def violation_helper(self, node):
        balance = self.calculate_balance(node)

        # if the tree is left heavy
        if balance > 1:
            # left-right heavy situation: left rotation on parent + right rotation on grandparent
            if self.calculate_balance(node.left_child) < 0:
                self.rotate_left(node.left_child)
            # otherwise it is left-left heavy and we only need the right rotation
            self.rotate_right(node)
        # if the tree is right heavy
        elif balance < -1:
            # right-left heavy situation: right rotation on parent + left rotation on grandparent
            if self.calculate_balance(node.right_child) > 0:
                self.rotate_right(node.right_child)
            # otherwise it is right-right heavy and we only need the left rotation
            self.rotate_left(node)

    def handle_violation(self, node):
        # check the nodes from the node we have inserted up to the root node
        while node is not None:
            node.height = max(self.calc_height(node.left_child),
                              self.calc_height(node.right_child)) + 1
            self.violation_helper(node)
            node = node.parent

    def rotate_right(self, node):
        print(f"Rotating to the right on node: {node.data}")

        temp_left_node = node.left_child
        t = temp_left_node.right_child

        temp_left_node.right_child = node
        node.left_child = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_child == node:
            temp_left_node.parent.left_child = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_child == node:
            temp_left_node.parent.right_child = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calc_height(node.left_child),
                          self.calc_height(node.right_child)) + 1
        temp_left_node.height = max(self.calc_height(
            temp_left_node.left_child), self.calc_height(temp_left_node.right_child)) + 1

    def rotate_left(self, node):
        print(f"Rotating to the left on node: {node.data}")

        temp_right_node = node.right_child
        t = temp_right_node.left_child

        temp_right_node.left_child = node
        node.right_child = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_child == node:
            temp_right_node.parent.left_child = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_child == node:
            temp_right_node.parent.right_child = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calc_height(node.right_child),
                          self.calc_height(node.right_child)) + 1
        temp_right_node.height = max(self.calc_height(
            temp_right_node.left_child), self.calc_height(temp_right_node.right_child)) + 1

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


avl = AVLTree()
avl.insert(32)
avl.insert(16)
avl.insert(48)
avl.insert(8)
avl.insert(24)
avl.insert(40)
avl.insert(56)
avl.insert(36)
avl.insert(44)
avl.insert(52)
avl.insert(60)
avl.insert(4)
avl.insert(58)
avl.insert(62)
avl.insert(-10)
avl.insert(-11)
avl.insert(-12)
avl.insert(-13)
avl.insert(-14)
avl.insert(-15)
avl.insert(-16)
avl.insert(-17)
avl.insert(-18)
avl.insert(-19)
avl.insert(-20)
avl.insert(-21)
avl.insert(-22)
avl.insert(-23)
avl.insert(-24)
avl.insert(-25)
avl.insert(-26)
avl.insert(-27)
avl.insert(-28)
avl.insert(-29)
avl.insert(-16)
avl.insert(-17)
avl.insert(-18)
avl.insert(-19)
avl.insert(-20)
avl.insert(-21)
avl.insert(-22)
avl.insert(-23)
avl.insert(-24)
avl.insert(-25)
avl.insert(-26)
avl.insert(-27)
avl.insert(-28)
avl.insert(-29)
avl.insert(600)
avl.insert(425)
avl.insert(1000)
avl.insert(6200)
avl.remove(4)
avl.remove(40)
avl.remove(48)
avl.remove(32)
avl.remove(-16)
avl.remove(-17)
avl.remove(-18)
avl.remove(-19)
avl.remove(-20)
avl.remove(-21)
avl.remove(-22)
avl.remove(-23)
avl.remove(-24)
avl.remove(-25)
avl.remove(-26)
avl.remove(-27)
avl.remove(-28)
avl.remove(-29)
avl.remove(-16)
avl.remove(-17)
avl.remove(-18)
avl.remove(-19)
avl.remove(-20)
avl.remove(-21)
avl.remove(-22)
avl.remove(-23)
avl.remove(-24)
avl.remove(-25)
avl.remove(-26)
avl.remove(-27)
avl.remove(-28)
avl.remove(-29)
print(avl.root.data)

avl.traverse()
print(avl.ordered)
