#!/bin/python3

import sys

num = int(input().strip())
l = []
while True:
    if num == 0:
        break
    rem = num % 2
    num = num//2 
    l.append(rem)

tmp = 0
big = 0
for el in l:
    if el == 1:
        tmp += 1
    elif el == 0:
        if tmp > big:
            big = tmp
        tmp = 0
if tmp > big:
    big = tmp
print(big)
     
