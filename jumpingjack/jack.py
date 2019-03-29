#!/bin/python3
import math
import os
import random
import re
import sys
import pdb
#
# Complete the 'maxStep' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def maxStep(n, k):
    #pdb.set_trace()
    #basecase
    if (n == 1 and k == 1):
        return 0
    res=0
    index=1
    flag=0
    while (1):
        for i in range(index, n+1):
            flag = 0
            res = res + i
            if (res == k):
                flag=1
                index+=1
                res=0
                break
        if (flag == 0):
            return (res)

if __name__ == '__main__':

    n = int(input().strip())

    k = int(input().strip())
    result = maxStep(n, k)

    print(str(result))
