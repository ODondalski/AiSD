class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def node(self, at):
        current = self.head
        for i in range(at):
            current = current.next
        return current

    def insert(self, value, after):
        current = self.head
        new_node = Node(value)
        while current.next is not None:
            if after == current:
                current.next = new_node
                new_node.next = current.next.next
            current = current.next

    def pop(self):
        deleted = self.head
        self.head = self.head.next
        return deleted

    def remove_last(self):
        deleted = self.tail
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.tail = current
        return deleted

    def remove(self, after):
        current = self.head
        while current.next is not None:
            if after == current:
                current.next = current.next.next
            current = current.next

    def print(self):
        if self.head is None:
            return "List empty"
        current = self.head
        lst = []
        while current.next is not None:
            lst.append(str(current.data))
            current = current.next
        lst.append(str(current.data))
        new_list = ' -> '.join(lst)
        return new_list

    def __len__(self):

linked_list = LinkedList()
assert linked_list.head is None
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)
linked_list.append(1)
linked_list.remove_last()
linked_list.remove_last()
print(linked_list.node(1).data)
print(linked_list.print())
print(f"node at 2 {linked_list.node(2)}")
print(f"head - {linked_list.head.data}")
print(f"tail - {linked_list.tail.data}")
