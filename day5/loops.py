#!/bin/python3

import sys


n = int(input().strip())
count = 1
while count <= 10:
    print('{0} x {1} = {2}'.format(n, count, n*count))
    count += 1
