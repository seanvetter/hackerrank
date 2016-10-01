#!/bin/python3

import sys


N = int(input().strip())
if N % 2 == 0: # even
    if N > 20:
        print("Not Weird")
    if N >= 2 and N <= 5:
        print("Not Weird")
    if N >= 6 and N <= 20:
        print('Weird')
else: # odd
    print('Weird')

    

