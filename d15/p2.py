import re
from collections import defaultdict, Counter
from copy import copy
from sys import maxsize

import time
start_time = time.time()

with open("input1.txt") as f:
    raw_data = f.readlines()
    data = []

    for raw_row in raw_data:
        row =[]
        for i in range(5):
            for idx, x in enumerate(raw_row.strip()):
                row.append((int(x)+i)%9 if int(x)+i >9 else int(x)+i)

        data.append(row)

    datas = []
    for i in range(5):
        for row1 in data:
            row = []
            for idx, x in enumerate(row1):
                row.append((int(x) + i) % 9 if int(x) + i > 9 else int(x) + i)
            datas.append(row)
    data = datas
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
            if len(global_arr) > k >= 0 and len(global_arr[0]) > m >= 0:
                value = global_arr[i][j] + data[k][m]
                if value < global_arr[k][m]:
                    global_arr[k][m] = value
                    stack.append([k,m])

        idx+=1
    print(global_arr[-1][-1])
print("--- %s seconds ---" % (time.time() - start_time))