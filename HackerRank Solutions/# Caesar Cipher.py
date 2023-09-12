# Caesar Cipher 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    # ascu values for characters
    temp = []  
    
    # convert char to ascii value 
    for char in s:
        temp.append(ord(char))
        
    # main logic - shifting
    for i in range(n):
        # uppercase - 65 - 90 
        if 65 <= temp[i] <= 90:
            temp[i] = (65 + (temp[i]-65+k)%26)
            # 65 - a 
            # 65 - 65 = (0 + 29) % 26 = 3
            # 65 + 3 = 68
        # lowercase - 97 - 112
        elif 97 <= temp[i] <= 122:
            temp[i] = (97 + (temp[i]-97+k)%26)
    
    return "".join(map(chr,temp))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
