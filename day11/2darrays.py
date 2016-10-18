#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

# when starting in upper left corner you just need to check for far right corners
totals = []
row_count = 0
while row_count < len(arr):
    if row_count+2 < len(arr):
        # we have enough rows to make an I
        col_count = 0
        row = arr[row_count]
        while col_count < len(row):
            if col_count+2 < len(row):
                # we have a row with 3 colums
                t1 = row[col_count] + row[col_count+1] + row[col_count+2]
                t2 = arr[row_count+1][col_count+1]
                t3 = arr[row_count+2][col_count] + arr[row_count+2][col_count+1]  + arr[row_count+2][col_count+2]
                totals.append(t1+t2+t3)
            col_count += 1
    row_count += 1

print(max(totals))
