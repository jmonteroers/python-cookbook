from __future__ import annotations
from typing import Any


class Node:
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


if __name__ == "__main__":
    root = Node(0)
    ch1 = Node(1)
    ch2 = Node(2)
    root.add_children(ch1, ch2)
    for ch in root:
        print(ch)

