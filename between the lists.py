#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    i = 0
    for j in range(max(a), min(b)+1):
        while j % a[i] == 0:
            i += 1



        array1.append(j)
    print(array1)
    array2 = []
    for j in b:
        for i in array1:
            if j % i != 0:
                break
            else:
                continue
        array2.append(j)
    print(array2)
    return len(array2)






if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)


