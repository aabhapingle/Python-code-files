#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    suma = 0
    sumb = 0
    i = 0
    for i in range(3):
        if a[i] < b[i]:
            sumb += 1
        elif a[i] == b[i]:
            pass
        else:
            suma += 1
    array = []
    array.append(suma)
    array.append(sumb)
    return array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
