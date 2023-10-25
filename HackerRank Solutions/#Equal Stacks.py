#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    # reverse elements in the stack
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    
    # find sum of each stack
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)
    
    # main logic
    while True:
        minheight = min(sum1, sum2, sum3)
        # base case
        if minheight == 0:
            return 0        
        
        # general case 
        if minheight < sum1:
            sum1 -= h1.pop()
        if minheight < sum2:
            sum2 -= h2.pop()
        if minheight < sum3:
            sum3 -= h3.pop()
            
        if sum1 == sum2 == sum3:
            return sum1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
