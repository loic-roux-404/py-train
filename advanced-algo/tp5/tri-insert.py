import sys
from os import path
sys.path.append(path.abspath(__file__ + '/../../modules'))

from tests import run

def tri_insert(int_list):
    # Traverse through 1 to len(arr)
    for i in range(1, len(int_list)):

        key = int_list[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < int_list[j] :
                int_list[j + 1] = int_list[j]
                j -= 1
        int_list[j + 1] = key

# 1.0s
run(tri_insert, [
    {'args': {'int_list': [14, 7, 3, 18, 23]}, 'result': [3, 7, 14, 18, 23]},
    {'args': {'int_list': [0.1, 4, 3, 3, 72]}, 'result': [0.1, 3, 3, 4, 72]},
    {'args': {'int_list': [120, 47, 3, 18, 1, 2.5]}, 'result': [1, 2.5, 3, 18, 47, 120]},
    {'args': {'int_list': [1, 2, 3, 4, 5]}, 'result': [1, 2, 3, 4, 5]},
    {'args': {'int_list': [5, 4, 3, 2, 1]}, 'result': [1, 2, 3, 4, 5]}
])
