from typing import Generic, TypeVar, Optional
import enum
from LinkedList import DoublyLinkedList

T = TypeVar('T')

class GraphType(enum.Enum):
    GRAPH_TYPE_DIRECTED = 0 # one way
    GRAPH_TYPE_UNDIRECTED = 1 # both ways

class Node(Generic[T]):
    def __init__(self, value: T):
        self._value = value
        self._neighbors: DoublyLinkedList["Node[T]"] = DoublyLinkedList()

    @property
    def neighbours(self) -> DoublyLinkedList["Node[T]"]:
        return self._neighbors

    @property
    def value(self) -> T:
        self._value

class Graph(Generic[T]):
    def __init__(self, graph_type: GraphType = GraphType.GRAPH_TYPE_UNDIRECTED):
        self._graph_type = graph_type
        self._nodes: Optional[Node[T]] = {}

    def append_node(self, value: T):
        if not value in self._nodes:
            self._nodes[value] = Node(value)

if __name__ == '__main__':
    hello = ""