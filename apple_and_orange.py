#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples2 = []
    oranges2 = []
    for _ in apples:
        _ += a
        apples2.append(_)

    for _ in oranges:
        _ += b
        oranges2.append(_)

    count_apples = 0
    count_oranges = 0
    for _ in apples2:
        if s <= _ <= t:
            count_apples += 1
        else:
            pass
    print(count_apples)

    for _ in oranges2:
        if s <= _ <= t:
            count_oranges += 1
        else:
            pass
    print(count_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
