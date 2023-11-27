#Hackerland_Radio_Transmitters
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

# 2 4 5 6 7 9 11 12
# loc = 2 + 2 = 4

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x. sort()
    count = 0
    i = 0
    
    while i < n:
        # first half
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
        
        # place the transmitter and increment
        i -= 1
        count += 1
               
        # second half
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
            
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
