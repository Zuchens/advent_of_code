"east (>) south (v) ."
from copy import copy
from dataclasses import dataclass


@dataclass
class Cucumber:
    side: str
    visited:bool = False

with open("input1.txt") as f:

    lines = []
    for row in f.readlines():
        elements = [Cucumber(element) if element != "." else None for element in row.strip()]
        lines.append(elements)

idx = 0
# number = 4
while True:
    lines0 = copy(lines)
    new_data = [[None for j in range(len(lines[i]))] for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] is None:
                continue
            if  lines[i][j].side == ">":
                if j+1 < len(lines[i]):
                    neighbour = j+1
                else:
                    neighbour = 0
                if lines[i][neighbour] is None:
                    new_data[i][neighbour] = lines[i][j]
                    new_data[i][j] = None
                else:
                    new_data[i][j] = lines[i][j]
            else:
                new_data[i][j] = lines[i][j]
    lines = new_data
    new_data = [[None for j in range(len(lines[i]))] for i in range(len(lines))]
    # for i in range(len(lines)):
    #     for j in range(len(lines[i])):
    #         if lines[i][j] is None:
    #             print(".",end="")
    #         else:
    #             print(lines[i][j].side, end="")
    #     print()
    # print()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] is None:
                continue
            if  lines[i][j].side == "v":
                if i+1 < len(lines):
                    neighbour = i+1
                else:
                    neighbour = 0
                if lines[neighbour][j] is None:
                    new_data[neighbour][j] = lines[i][j]
                    new_data[i][j] = None
                else:
                    new_data[i][j] = lines[i][j]
            else:
                new_data[i][j] = lines[i][j]


    diff = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if new_data[i][j] != lines0[i][j]:
                diff+=1
    if diff == 0:
        break
    # print()
    lines = new_data

    # for i in range(len(lines)):
    #     for j in range(len(lines[i])):
    #         if lines[i][j] is None:
    #             print(".", end="")
    #         else:
    #             print(lines[i][j].side, end="")
    #     print()
    # print()
    idx+=1

print(idx+1)


