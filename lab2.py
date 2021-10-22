from typing import Any


class Node:
    data: Any
    next: 'Node'

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        current = self.head
        lst = []
        while current.next is not None:
            lst.append(str(current.data))
            current = current.next
        lst.append(str(current.data))
        new_list = ' -> '.join(lst)
        return new_list

    def __len__(self):
        current = self.head
        counter = 0
        if self.head is not None:
            while current.next is not None:
                current = current.next
                counter += 1
            return counter + 1
        return counter

    def push(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def node(self, at: int) -> Node:
        current = self.head
        for i in range(at):
            current = current.next
        return current

    def insert(self, value: Any, after: Node) -> None:
        current = self.head
        new_node = Node(value)
        while current.next is not None:
            if after == current:
                temp = current.next
                current.next = new_node
                new_node.next = temp
            current = current.next

    def pop(self) -> Any:
        deleted = self.head
        self.head = self.head.next
        return deleted.data

    def remove_last(self) -> Any:
        deleted = self.tail
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        return deleted.data

    def remove(self, after: Node) -> Any:
        current = self.head
        while current.next is not None:
            if after == current:
                if current.next.next is None:
                    current.next = current.next.next
                    self.tail = current
                else:
                    current.next = current.next.next
                return
            current = current.next

"""
linked_list = LinkedList()
assert linked_list.head is None
linked_list.push(1)
linked_list.push(0)
# print(linked_list)
assert str(linked_list) == '0 -> 1'
linked_list.append(9)
linked_list.append(10)
assert str(linked_list) == '0 -> 1 -> 9 -> 10'
# print(linked_list)
middle_node = linked_list.node(at=1)
linked_list.insert(5, after=middle_node)
assert str(linked_list) == '0 -> 1 -> 5 -> 9 -> 10'
# print(str(linked_list))
first_element = linked_list.node(at=0)
returned_first_element = linked_list.pop()
assert first_element.data == returned_first_element
last_element = linked_list.node(at=3)
returned_last_element = linked_list.remove_last()
assert last_element.data == returned_last_element
assert str(linked_list) == '1 -> 5 -> 9'
# print(linked_list)
second_node = linked_list.node(at=1)
linked_list.remove(second_node)
assert str(linked_list) == '1 -> 5'
# print(linked_list)
"""

linked_list = LinkedList()

linked_list.push(5)
linked_list.push(2)
print(linked_list)


class Stack:
    storage: LinkedList

    def __init__(self):
        self.storage = LinkedList()

    def __str__(self):
        lst = []
        current = self.storage.head
        while current is not None:
            lst.append(str(current.data))
            current = current.next
        return '\n'.join(lst)

    def push(self, element: Any) -> None:
        self.storage.push(element)

    def pop(self) -> Any:
        return self.storage.pop()

    def __len__(self):
        return len(self.storage)


stack = Stack()

assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)
print(stack)
assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2
print(stack)


class Queue:
    storage: LinkedList

    def __len__(self):
        return len(self.storage)

    def __init__(self):
        self.storage = LinkedList()

    def __str__(self):
        current = self.storage.head
        lst = []
        while current is not None:
            lst.append(str(current.data))
            current = current.next
        new_list = ', '.join(lst)
        return new_list

    def peek(self) -> Any:
        return self.storage.head.data

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)

    def dequeue(self) -> Any:
        return self.storage.pop()


queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
print(queue)
assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
print(queue)

