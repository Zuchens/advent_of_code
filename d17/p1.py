import re
from collections import defaultdict, Counter
from copy import copy
from functools import reduce
from sys import maxsize

import time


with open("input1.txt") as f:
    raw_data = f.read().strip()
    matched_value = re.match("target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)", raw_data)
    x0 = int(matched_value.group(1))
    x1 = int(matched_value.group(2))
    y0 = int(matched_value.group(3))
    y1 = int(matched_value.group(4))
a = 1


set_value=set()
xp =0
yp =0
max_vel  = -1*maxsize
for i in range(x1+1):
    a = i
    for j in range(-500,500):
        xp = 0
        yp = 0
        i = a
        b = j
        # print(a,b)
        max_vel_local = -1 * maxsize
        prev_shortest_odc = maxsize
        shortest_odc = min((xp - x0) ** 2 + (yp - y0) ** 2,
                           (xp - x0) ** 2 + (yp - y1) ** 2,
                           (xp - x1) ** 2 + (yp - y0) ** 2,
                           (xp - x1) ** 2 + (yp - y1) ** 2)
        k = 0
        while xp <= x1 and yp >= y0:
            if x0 <= xp <= x1 and y0 <= yp <= y1:
                set_value.add(f"{a},{b}")
                if max_vel < max_vel_local:
                    max_vel = max_vel_local
                break
            k+=1
            xp = xp+i
            yp = yp+j
            if i > 0:
                i = i-1
            elif i < 0:
                i = i+1
            else:
                i = 0
            j = j-1
            if max_vel_local < yp:
                max_vel_local = yp
            prev_shortest_odc = shortest_odc
            shortest_odc = min((xp -x0)**2 + (yp -y0)**2,
                               (xp - x0) ** 2 + (yp - y1) ** 2,
            (xp - x1) ** 2 + (yp - y0) ** 2,
            (xp - x1) ** 2 + (yp - y1) ** 2)
        c = 1
print(set_value)
print(len(set_value))

print(max_vel)