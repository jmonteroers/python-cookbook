from __future__ import annotations
from typing import Any, Iterator, Optional, Union


class Node:
    """Easiest way to implement iteration is to use a generator function"""
    def __init__(self, value: Any) -> None:
        self._value = value
        self._children = []
    
    def __repr__(self) -> None:
        return "Node({!r})".format(self._value)
    
    def add_children(self, *children: Node) -> Node:
        for child in children:
            self._children.append(child)
    
    def __iter__(self) -> None:
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


class DepthFirstIterator:
    def __init__(self, start_node) -> None:
        self._node = start_node
        self._children_iter: Iterator[AlternativeNode] = None
        self._child_iter: Optional[DepthFirstIterator] = None
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Union[DepthFirstIterator, AlternativeNode]:
        # initial case, create iterator from children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # processing a child
        elif self._child_iter:
            nextchild = next(self._child_iter, None)
            if nextchild is None:
                self._child_iter = None
                return next(self)
            return nextchild
        # advance to next child, start iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


class AlternativeNode(Node):
    """Python's iterator protocol requires to return an object that implements a __next__ operation and 
    signals a StopIteration exception to signal completion"""
    def depth_first(self):
        return DepthFirstIterator(self)


if __name__ == "__main__":
    # Best option
    print("**Best option**")
    root = Node(0)
    ch1 = Node(1)
    ch2 = Node(2)
    gch1 = Node(3)
    gch2 = Node(4)
    gch3 = Node(5)
    gch4 = Node(6)
    root.add_children(ch1, ch2)
    ch1.add_children(gch1, gch2, gch3)
    ch2.add_children(gch4)
    # expected: 0, 1, 3, 4, 5, 2, 6
    for ch in root.depth_first():
        print(ch)
    
    print("**Alternative option**")
    root = AlternativeNode(0)
    ch1 = AlternativeNode(1)
    ch2 = AlternativeNode(2)
    gch1 = AlternativeNode(3)
    gch2 = AlternativeNode(4)
    gch3 = AlternativeNode(5)
    gch4 = AlternativeNode(6)
    root.add_children(ch1, ch2)
    ch1.add_children(gch1, gch2, gch3)
    ch2.add_children(gch4)
    # expected: 0, 1, 3, 4, 5, 2, 6
    for ch in root.depth_first():
        print(ch)