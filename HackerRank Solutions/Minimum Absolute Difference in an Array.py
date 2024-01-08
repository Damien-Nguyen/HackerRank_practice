Minimum Absolute Difference in an Array
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    min_diff = sys.maxsize
    for i in range(1, len(arr)):
        min_diff = min(min_diff, abs(arr[i-1]-arr[i]))
        
    return min_diff
    
# 1 -3 71 68 17
# -3 1 17 68  71 - sort
#    4 16 51  3 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
