from typing import Iterator

def manually_consume_iterator(iterator: Iterator) -> None:
    print("Starting manual consumption of iterator")
    try:
        while True:
            item = next(iterator)
            print(item, end='')
    except StopIteration:
        print("Finishing iteration by catching the StopIteration error")


def manually_consume_iterator_alt(iterator: Iterator) -> None:
    """Pass a second argument to next. Need to make sure that iterator never contains that value!"""
    print("Starting manual consumption of iterator")
    while True:
        item = next(iterator, None)
        if item is None:
            print("Finishing iteration by using None")
            break
        print(item, end='')


if __name__ == "__main__":
    path = '../data/sample.txt'
    with open(path) as fd:
        print("**First option:**")
        manually_consume_iterator(fd)
    with open(path) as fd:
        print("**Second option:**")
        manually_consume_iterator_alt(fd)
        