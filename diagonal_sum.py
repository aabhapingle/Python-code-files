#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    sumr = 0
    for i in range(n-1,-1,-1):
        for j in range(0,n):
            if i+j == n-1:
                sumr += arr[i][j]
    suml = 0
    for i in range(0,n):
        for j in range(n-1,-1,-1):
            if i == j:
                suml += arr[i][j]

    return abs(suml - sumr)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
