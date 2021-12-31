import os
import fnmatch
import gzip
import re
from typing import Iterator, IO


def gen_find(file_pattern: str, root_folder: str) -> Iterator[str]:
    for path, dirlist, filelist in os.walk(root_folder):
        for name in fnmatch.filter(filelist, file_pattern):
            yield os.path.join(path, name)


def gen_opener(filenames: Iterator[str]) -> Iterator[IO]:
    for name in filenames:
        if name.endswith(".gz"):
            f = gzip.open(name, "rt")
        else:
            f = open(name, "r")
        yield f
        # nice touch, to ensure that file is closed when retrieving next file
        f.close()


def gen_concatenate(iterators: Iterator[Iterator]) -> Iterator:
    for it in iterators:
        yield from it


def gen_grep(pattern, lines: Iterator[str]):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


if __name__ == "__main__":
    input_path = '../data/pipeline'
    ## Extend pipeline with generator expressions
    filenames = gen_find("access_*", input_path)  
    files = gen_opener(filenames)
    lines = gen_concatenate(files)
    robot_lines = gen_grep('robot', lines)
    for path in gen_find("access*", input_path):
        print(path)
    for line in robot_lines:
        print(line)
    
    filenames = gen_find("access_*", input_path)  
    files = gen_opener(filenames)
    lines = gen_concatenate(files)
    robot_lines = gen_grep('robot', lines)
    bytecolumn = (line.rsplit(" ", 1)[1] for line in robot_lines)
    file_bytes = (int(x) for x in bytecolumn if x != '-')
    print('Total', sum(file_bytes))  
