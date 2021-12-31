from typing import Iterator

def manually_consume_iterator(iterator: Iterator) -> None:
    try:
        while True:
            item = next(iterator)
            print(item, end='')
    except StopIteration:
        print("Finishing iteration by catching the StopIteration error")
