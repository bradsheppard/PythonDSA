from typing import Iterable, Optional


class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next: Optional[ListNode] = None


class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self) -> Iterable[int]:
        current = self.head

        while current:
            yield current.val
            current = current.next

    def insert_tail(self, val: int):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = new_node

    def insert_head(self, val: int):
        new_node = ListNode(val)
        
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node


def test_linked_list_insert_tail():
    linked_list = LinkedList()
    linked_list.insert_tail(1)
    linked_list.insert_tail(2)
    linked_list.insert_tail(3)

    pos = 1
    current = linked_list.head

    while current:
        assert pos == current.val
        current = current.next
        pos += 1


def test_linked_list_insert_head():
    linked_list = LinkedList()
    linked_list.insert_head(1)
    linked_list.insert_head(2)
    linked_list.insert_head(3)

    pos = 3
    current = linked_list.head

    while current:
        assert pos == current.val
        current = current.next
        pos -= 1
