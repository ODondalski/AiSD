class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
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
        if self.head is None:
            return 0
        else:
            while current.next is not None:
                current = current.next
                counter += 1
            return counter + 1

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
                temp = current.next
                current.next = new_node
                new_node.next = temp
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
                if current.next.next is None:
                    current.next = current.next.next
                    self.tail = current
                else:
                    current.next = current.next.next
                return
            current = current.next

    def print(self):
        if self.head is None:
            print("List empty")
        current = self.head
        lst = []
        while current.next is not None:
            lst.append(str(current.data))
            current = current.next
        lst.append(str(current.data))
        new_list = ' -> '.join(lst)
        print(new_list)


linked_list = LinkedList()
assert linked_list.head is None
linked_list.push(1)
linked_list.push(0)
linked_list.print()
assert str(linked_list) == '0 -> 1'
linked_list.append(9)
linked_list.append(10)
assert str(linked_list) == '0 -> 1 -> 9 -> 10'
linked_list.print()
middle_node = linked_list.node(at=1)
linked_list.insert(5, after=middle_node)
linked_list.print()
first_element = linked_list.node(at=0)
returned_first_element = linked_list.pop()
assert first_element.data == returned_first_element.data
last_element = linked_list.node(at=3)
returned_last_element = linked_list.remove_last()
assert last_element.data == returned_last_element.data
linked_list.print()
second_node = linked_list.node(at=1)
linked_list.remove(second_node)
assert str(linked_list) == '1 -> 5'
linked_list.print()
print(f"size of list - {linked_list.__len__()}")
