import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    to_bin = bin(n)[2:]
    split = to_bin.split('0')
    
    maxi = 0
    for group in split:
        
        length = len(group)
        if length > maxi:
            maxi = length
            
    print(maxi) 
