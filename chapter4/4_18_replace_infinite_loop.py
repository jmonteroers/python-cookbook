from typing import IO


def while_infinite_loop(f: IO) -> None:
    while chunk := f.read(10):
        print(chunk)


def iterable_loop(f: IO[str]) -> None:
    """Risk of infinite loop is still possible, if wrong second argument provided to `iter"""
    for chunk in iter(lambda: f.read(10), "e"):
        print(chunk)


if __name__ == "__main__":
    print("**While option**")
    with open('../data/sample.txt') as fd:
        while_infinite_loop(fd)
    print("**Iterable option**")
    with open('../data/sample.txt') as fd:
        iterable_loop(fd)