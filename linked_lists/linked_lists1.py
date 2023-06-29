from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: Any
    next: 'Node' = None


@dataclass
class LinkedList:
    head: Node = None
    tail: Node = None

    def push(self, value: Any) -> None:
        new_head = Node(value)
        new_head.next = self.head

        if self.head is None and self.tail is None:
            self.tail = new_head

        self.head = new_head

    def push_back(self, value: Any) -> None:
        new_tail = Node(value)
        if len(self) > 0:
            self.tail.next = new_tail
        else:
            self.head = new_tail

        self.tail = new_tail

    def __len__(self) -> int:
        curr = self.head
        counter = 0
        while curr:
            counter += 1
            curr = curr.next

        return counter

    def __str__(self) -> str:
        output = ''
        curr = self.head

        while curr:
            if curr == self.tail:
                output += str(curr.value)
            else:
                output += str(curr.value) + ' -> '
            curr = curr.next
        return output

    def find_by_idx(self, idx: int) -> Node:
        counter = 0
        curr = self.head
        while counter != idx and curr is not None:
            curr = curr.next
            counter += 1

        return curr

    def remove_last(self) -> Any:
        if self.head is self.tail:
            self.tail, self.head = None
        removed_node = self.tail
        new_tail = self.find_by_idx(idx=len(self) - 2)
        new_tail.next = None

        self.tail = new_tail

        return removed_node.value

    def remove(self, after_idx: int) -> Any:
        after = self.find_by_idx(after_idx)

        if after is self.tail:
            return None

        if after.next is self.tail:
            return self.remove_last()

        removed_node = after.next
        after.next = after.next.next

        return removed_node.value

    def pop(self) -> Any:
        if len(self) == 0:
            return None

        erased_node = self.head

        if self.head is self.tail:
            self.tail = self.tail.next

        self.head = self.head.next
        return erased_node.value

    def clean(self):
        counter = 0
        curr = self.head
        uniques = []

        while curr:
            if curr.value in uniques:
                self.remove(counter - 1)
                counter -= 1
            else:
                uniques.append(curr.value)
            counter += 1
            curr = curr.next
        print(uniques)
        return self



linked_list = LinkedList()
taking_numbers = True
while taking_numbers:
    try:
        number = int(input())
    except ValueError:
        taking_numbers = False
    else:
        linked_list.push_back(number)
linked_list_cleaned = linked_list.clean()
print(linked_list_cleaned)