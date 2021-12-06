#### TASK 1
from dataclasses import dataclass


@dataclass
class Line:
    from_x: int
    from_y: int
    to_x: int
    to_y: int
with open("input1.txt") as f:
    data = [ x.strip() for x in f.readlines()]
lines = []
largest_x = -1
largest_y = -1
for row in data:
    from_row, to_row = row.split("->")
    from_x, from_y = from_row.strip().split(",")
    to_x, to_y = to_row.strip().split(",")
    line = Line(int(from_x),int(from_y),int(to_x), int(to_y))
    lines.append(line)
    if line.to_x> largest_x:
        largest_x = line.to_x
    if line.to_y> largest_y:
        largest_y = line.to_y
    if line.from_y> largest_y:
        largest_y = line.from_y
    if line.from_x> largest_x:
        largest_x = line.from_x

data =[[0 for _1 in range(largest_x+1)] for _2 in range(largest_y+1)]
for line in lines:
    if line.to_y == line.from_y:
        if line.from_x > line.to_x:
            for i in range(line.to_x, line.from_x+1):
                data[line.to_y][i]+=1
        else:
            for i in range(line.from_x, line.to_x+1):
                data[line.to_y][i]+=1
    if line.to_x == line.from_x:
        if line.from_y > line.to_y:
            for i in range(line.to_y, line.from_y+1):
                data[i][line.to_x]+=1
        else:
            for i in range(line.from_y, line.to_y+1):
                data[i][line.to_x]+=1

large = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] >=2:
            large+=1
print(large)



