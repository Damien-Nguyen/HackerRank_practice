#Queries_with_fixed_length
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

def solve(arr, queries):
    # Write your code here
    result = []
    for d in queries:
        maxnum = max(arr[:d])
        minnum = maxnum
        
        # main logic
        for i in range(d, len(arr)):
            # if element goes out of window
            if arr[i-d] == maxnum:
                maxnum = max(arr[i-d+1:i+1])
            # new element is greater than maxnum
            elif arr[i] > maxnum:
                maxnum = arr[i]
                
            # update overall minmum
            if maxnum < minnum:
                minnum = maxnum
                
        result.append(minnum)
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
