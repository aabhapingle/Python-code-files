#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    array = s.split(':')
    if array[-1][-2:] == 'AM':
        if array[0] == '12':
            return '00' + s[2:8]
        else:
            return s[:-2]
    else:
        if array[0] == '12':
            return s[:-2]
        else:
            return str(int(array[0]) + 12) + s[2:-2]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
