# Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    def helper(n):
        total = 0
        for num in n:
            total += int(num)
        total = str(total)
        if len(total) == 1:
            return total 
        else:
            return helper(total)
        
    p = str(helper(n)*k)
    return helper(p)

# 123 3
# 123123123
# helper(123123123)
# total = 1+2+3+1+2+3+1+2+3 = 18
# helper(18)
# total = 1+8 = 9
# return 9 (as it's only one digit)

# optimized code
# helper(123)
# total = 1+2+3 = 6
# p = 666
# helper(666)
# total = 6+6+6 = 18
# helper(18)
# total = 1+8 = 9
#return 9 (as it's only one digit)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
