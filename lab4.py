from typing import Any, List, Callable, Union
from lab3 import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if len(self.children) == 0:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue = Queue()
        for child in self.children:
            queue.enqueue(child)
        while queue.__len__() != 0:
            element = queue.dequeue()
            visit(element)
            for child in self.children:
                queue.enqueue(child)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if value in self.for_each_deep_first(value):
            


class Tree:
    root: TreeNode

    def __init__(self, root=None):
        self.root = root

    def add(self, value: Any, parent_name: Any) -> None:
        new_node = TreeNode(parent_name)
        new_node.children.append(value)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.for_each_deep_first(visit)


tree = Tree("F")
tree.add("A", "B")
tree.add("D", "B")
