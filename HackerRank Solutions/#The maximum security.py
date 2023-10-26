#The maximum security 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # Write your code here
    subSequenceSum = 0
    subArraySum = -sys.maxsize
    subSequenceTemp = -sys.maxsize
    subArrayTemp = 0
    
    # iterate the array
    for num in arr:
        # maximum subsequence
        if num > 0:
            subSequenceSum += num
        else:
            subSequenceTemp = max(subSequenceTemp, num)
        
        # maximum subarray
        subArrayTemp = subArrayTemp + num
        if subArrayTemp > subArraySum:
            subArraySum = subArrayTemp
            
        if subArrayTemp < 0:
            subArrayTemp = 0
            
    if subSequenceSum == 0:
        subSequenceSum = subSequenceTemp
        
    return subArraySum, subSequenceSum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
