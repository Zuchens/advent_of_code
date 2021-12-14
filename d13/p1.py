import re
from collections import defaultdict
from copy import copy
from sys import maxsize

# with open("input1.txt") as f:
with open("input1.txt") as f:
    raw_data = f.readlines()
    rows = []
    min_valuex = 0
    min_valuey = 0
    folds = {"x": [], "y": []}

    folds_list = []
    for raw_row in raw_data:
        if not raw_row.strip():
            continue
        if raw_row.startswith("fold"):
            matched = re.match("fold along (.)=(\d+)", raw_row.strip())
            folds[matched.group(1)].append(int(matched.group(2)))
            folds_list.append([matched.group(1), int(matched.group(2))])
        else:
            x, y = raw_row.strip().split(",")
            if min_valuex < int(x):
                min_valuex = int(x)
            if min_valuey < int(y):
                min_valuey = int(y)
            rows.append(tuple([int(x), int(y)]))
data = [[0 for i in range(min_valuex + 1)] for j in range(min_valuey + 1)]
for row in rows:
    data[row[1]][row[0]] = 1

print("-------------")
for fold in folds_list:
    xy, num = fold
    if xy == "x":
        for i in range(len(data)):
            for j in range(num):
                if len(data[0]) > 2*num-j and data[i][2 * num - j] == 1:
                    data[i][j] = data[i][2 * num - j]

        data2 = []
        for i in range(len(data)):
            data2.append([data[i][j] for j in range(num)])
        data = data2
    if xy == "y":
        for i in range(num):
            for j in range(len(data[0])):
                if len(data) > 2*num-i and data[2 * num - i][j] == 1:
                    data[i][j] = data[2 * num - i][j]
        data2 = []
        for i in range(num):
            data2.append([data[i][j] for j in range(len(data[0]))])
        data = data2

dots = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if j % 5 == 0 and j != 0:
            print("  ", end="")
        if data[i][j] == 1:
            print("#", end="")
        else:
            print(".", end="")
    print("")
print(dots)
