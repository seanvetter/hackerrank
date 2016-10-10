#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
rev = []
for n in reversed(arr):
    rev.append(n)
print(" ".join(str(n) for n in rev))
