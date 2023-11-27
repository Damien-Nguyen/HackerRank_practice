#Sum VS XOR 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#
# 4 - 100 - 262 = 4
# 5 - 101 - 2^1 - 2 
# 10 - 1010 - 2^2 - 4
# if you have logic, validate with custom testcase


def sumXor(n):
    # Write your code here
    result = 1
    while n:
        b = n&1 # check if odd or even 
        n >>= 1 # divide by 2 
        if b==0:
            result *= 2
    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
