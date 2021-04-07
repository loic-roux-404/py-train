import sys
from os import path
sys.path.append(path.abspath(__file__ + '/../../modules'))

from tests import run

def tri_iteratif(int_list):
    for i in range(len(int_list)):
        min_index = i

        for j in range(i + 1, len(int_list)):
            print(min_index)
            if int_list[min_index] > int_list[j]:
                min_index = j

        int_list[i], int_list[min_index] = int_list[min_index], int_list[i]

    return int_list

run(tri_iteratif, [
    {'args': {'int_list': [14, 7, 3, 18, 23]}, 'result': [3, 7, 14, 18, 23]},
    {'args': {'int_list': [0.1, 4, 3, 3, 72]}, 'result': [0.1, 3, 3, 4, 72]},
    {'args': {'int_list': [120, 47, 3, 18, 1, 2.5]}, 'result': [1, 2.5, 3, 18, 47, 120]},
    {'args': {'int_list': [1, 2, 3, 4, 5]}, 'result': [1, 2, 3, 4, 5]},
    {'args': {'int_list': [5, 4, 3, 2, 1]}, 'result': [1, 2, 3, 4, 5]}
])
