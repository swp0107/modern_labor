#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lastLetters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING word as parameter.
#

def lastLetters(word):
    last = ''
    last = last + word[-1]
    last = last + ' '
    last = last + word[-2]
    return last

if __name__ == '__main__':

    word = input()

    result = lastLetters(word)

    print(result)
