#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    all_sums = []
    for i in range(0, len(ar)):
        for j in range(i+1, len(ar)):
            all_sums.append(ar[i] + ar[j])

    print(all_sums)
    print(len(all_sums))

    count = 0
    for _ in all_sums:
        if _ % k == 0:
            count += 1

    return count


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)