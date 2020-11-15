#!/usr/bin/env python

import sys
sys.setrecursionlimit(1000)

# Desk
desk = [[0] * 3] * 3
print(desk)

# recurse
i = 0
depth = 3


def recurseFunc():
    global i
    global depth
    if depth <= i:
        return

    print(desk)
    i += 1
    recurseFunc()


recurseFunc()

# factorial
def coeff(n, k):
    if k == 0 or k == n:
        return 1
    return coeff(n - 1, k - 1) + coeff(n - 1, k)


n, k = (49, 5)

print(coeff(n, k))
