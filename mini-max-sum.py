#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    a = sum(arr) - arr[4]
    b = sum(arr) - arr[0]
    print(a,b)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
