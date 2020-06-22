#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    a=0
    b=0
    c=0
    for i in arr:
        if i < 0:
            b += 1
        elif i == 0:
            c += 1
        else:
            a += 1
    print(round(a / n, 6))
    print(round(b / n, 6))
    print(round(c / n, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
