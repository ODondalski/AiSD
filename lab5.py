from typing import Any, Callable, List


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

    def traverse_in_order(self, visit: Callable[[Any, int], None], level=0):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit, level + 1)
        visit(self, level)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit, level + 1)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any, int], None], level=0):
        visit(self, level)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit, level + 1)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit, level + 1)

    def __str__(self):
        return str(self.value)


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

    def show(self):
        def _show(show_node: BinaryNode, level):
            print(' ' * 3 * level + '->', show_node.value)

        self.traverse_in_order(_show)


def right_line(tree_node: BinaryTree) -> List[BinaryNode]:
    lst = []
    if tree_node.root is not None:
        lst.append(tree_node.root.value)

    def _right_line(node: BinaryNode):
        if node.right_child is not None:
            lst.append(node.right_child.value)
            _right_line(node.right_child)

    def _right_line2(node: BinaryNode, level):
        if level > len(lst) - 1:
            lst.append(node.value)

    _right_line(tree_node.root)
    tree_node.root.traverse_pre_order(_right_line2)
    return lst


"""
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
print(right_line(tree))
tree.show()
"""
"""
tree = BinaryTree(1)
tree.root.add_right_child(3)
tree.root.right_child.add_right_child(7)
tree.root.add_left_child(2)
tree.root.left_child.add_right_child(5)
tree.root.left_child.add_left_child(4)
tree.root.left_child.left_child.add_right_child(9)
tree.root.left_child.left_child.add_left_child(8)
print(right_line(tree))
tree.show()
"""
