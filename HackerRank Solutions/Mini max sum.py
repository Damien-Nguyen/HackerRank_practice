Mini max sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    s = 0
    minnum = 999999999999
    maxnum = 0 
    n = len(arr)
    for i in range(n):
        s += arr[i]
        minnum = min(minnum, arr[i])
        maxnum = max(maxnum, arr[i])
    print(s-maxnum, s-minnum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
