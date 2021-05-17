import sys
from os import path
from time import time
sys.path.append(path.abspath(__file__ + '/../../modules'))

from tests import run

def tri_bulle(int_list):

    n = len(int_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]

    return int_list

# 3.0s
run(tri_bulle, [
    {'args': {'int_list': [14, 7, 3, 18, 23]}, 'result': [3, 7, 14, 18, 23]},
    {'args': {'int_list': [0.1, 4, 3, 3, 72]}, 'result': [0.1, 3, 3, 4, 72]},
    {'args': {'int_list': [120, 47, 3, 18, 1, 2.5]}, 'result': [1, 2.5, 3, 18, 47, 120]},
    {'args': {'int_list': [1, 2, 3, 4, 5]}, 'result': [1, 2, 3, 4, 5]},
    {'args': {'int_list': [5, 4, 3, 2, 1]}, 'result': [1, 2, 3, 4, 5]}
])
