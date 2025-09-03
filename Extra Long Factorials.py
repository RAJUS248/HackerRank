#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    if n == 0 or n == 1:
        return 1
    return extraLongFactorials(n-1) * n

if __name__ == '__main__':
    n = int(input().strip())

    print(extraLongFactorials(n))
