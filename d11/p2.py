import itertools
from dataclasses import dataclass


@dataclass
class Point:
    i: int
    j: int
    value: int
    flashed: bool = False


with open("input1_example.txt") as f:
    raw_data = f.readlines()
    data = []
    for i, raw_row in enumerate(raw_data):
        row = []
        for j, element in enumerate(raw_row.strip()):
            row.append(Point(i=i, j=j, value=int(element.strip())))
        data.append(row)

steps = 0
while True:
    steps = steps+1
    stack = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j].value += 1
            if data[i][j].value > 9:
                data[i][j].flashed = True
                stack[f"{i}{j}"] = data[i][j]

    while stack:

        element = stack.pop(list(stack.keys())[-1])
        for k, v in list(itertools.product([-1, 0, 1], [-1, 0, 1])):
            i1 = element.i + k
            j1 = element.j + v
            if i1 >= 0 and j1 >= 0 and i1 < len(data) and j1 < len(data[0]):
                data[i1][j1].value += 1
                if data[i1][j1].value > 9 and data[i1][j1].flashed == False:
                    stack[f"{i1}{j1}"] = data[i1][j1]
                    data[i1][j1].flashed = True
    all_flashes = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j].flashed = False
            if data[i][j].value > 9:
                data[i][j].value = 0
                all_flashes+=1
    if all_flashes == len(data)*len(data[0]):
        print(steps)
        break