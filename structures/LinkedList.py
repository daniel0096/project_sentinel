from typing import Any, TypeVar, TypeAlias, Optional, Iterator, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, vlue: T):
        self._value: T = vlue
        self._next: Optional["Node[T]"] = None
        self._prev: Optional["Node[T]"] = None

class DoublyLinkedList(Generic[T]):
    def __init__(self, head: Optional[Node[T]] = None, tail: Optional[Node[T]] = None):
        self._head: Optional[Node[T]] = head
        self._tail: Optional[Node[T]] = tail

    def append(self, value: T) -> None:
        node: Node[T] = Node(value)

        if not self._head:
            self._head = node
            self._tail = node
            return

        assert self._tail is not None
        self._tail._next = node

        node._prev = self._tail
        self._tail = node

    def pop_back(self) -> None:
        if not self._tail:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None
            return

        assert self._tail is not None
        new_tail = self._tail._prev # current tail
        new_tail._next = None # set next element at new tail as None
        self._tail = new_tail # current tail = new_tail

    def pop_front(self) -> None:
        if not self._head:
            return

        if self._head is self._tail:
            self._head = None
            self._tail = None

        assert self._head is not None
        new_head = self._head._next
        new_head._prev = None
        self._head = new_head

    def at(self, index: int) -> T:
        if index < 0:
            raise IndexError("Index < 0")

        for idx, value in enumerate(self):
            if idx == index:
                return value
        raise IndexError("Out of range")

    def __iter__(self) -> Iterator[T]:
        current = self._head

        while current is not None:
            yield current._value
            current = current._next

if __name__ == '__main__':    
    lst = DoublyLinkedList[str]()
    lst.append("node")
    lst.append("hello")
    print(lst.at(0))
    lst.pop_front()
    print(lst.at(0))
    lst.append("test")
    lst.append(1)
    lst.append(10)
    lst.append([10,10,10])

    print(f"4th element {lst.at(3)}")

    for element in lst:
        print(element)