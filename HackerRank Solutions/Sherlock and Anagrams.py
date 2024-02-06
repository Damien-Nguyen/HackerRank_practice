Sherlock and Anagrams  
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    res = 0
    for i in range(1, len(s)):
        d = {}
        for j in range(len(s)-i+1):
            sub = ''.join(sorted(s[j:j+i]))
            if sub not in d:
                d[sub]=1
            else:
                d[sub]+=1
            res+=d[sub]-1
    return res
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
