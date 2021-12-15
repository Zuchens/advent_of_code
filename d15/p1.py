import re
from collections import defaultdict, Counter
from copy import copy
from sys import maxsize


# with open("input1.txt") as f:
with open("input1.txt") as f:
    raw_data = f.readlines()
    data = []
    for raw_row in raw_data:
        row = [int(x) for x in raw_row.strip()]
        data.append(row)
    global_arr = [[maxsize for x in row] for row in data]
    stack = list()
    stack.append([0,0])
    global_arr[0][0] = 0
    idx = 0
    while stack:

        element = stack.pop(0)
        i = element[0]
        j = element[1]
        neigh = [[i-1,j], [i+1,j],[i,j-1],[i,j+1]]
        for k,m in neigh:
            if len(global_arr) > k >= 0 and m< len(global_arr[0]) and m >=0:
                value = global_arr[i][j] + data[k][m]
                if value < global_arr[k][m]:
                    global_arr[k][m] = value
                    stack.append([k,m])

        idx+=1
        if  idx %100000 == 0:
            for row in global_arr:
                print(row)
            print("")
    for row in global_arr:
        print(row)
