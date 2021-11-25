import os
from typing import List

def write_to_file(file: str, content) -> None:
    decomp_file_path = file.split('/')

    if len(decomp_file_path) > 1:
        directory = os.path.join(*file.split('/')[:len(decomp_file_path)-1])
        if os.path.isdir(directory):
            return
        os.makedirs(directory)
    # writing to file
    file1 = open(file, 'w')
    file1.writelines(content)
    file1.close()

def read_file(file: str) -> List[any]:
    try:
        io = open(file, 'r')
        return io.readlines()
    except IOError as e:
        print(e)
        return

def print_lines(l: List[any]) -> None:
    count = 0
    # Strips the newline character
    for line in l:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
