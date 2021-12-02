from typing import Any, Callable


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.traverse_post_order(visit)
        if self.right_child is not None:
            self.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.traverse_pre_order(visit)
        if self.right_child is not None:
            self.traverse_pre_order(visit)

    def __str__(self):
        return self.value


class BinaryTree:
    root: BinaryNode

    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


tree = BinaryTree(10)
tree.root.add_right_child(2)
tree.root.right_child.add_right_child(6)
tree.root.right_child.add_left_child(4)
tree.root.add_left_child(9)
tree.root.left_child.add_right_child(3)
tree.root.left_child.add_left_child(1)
assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True
