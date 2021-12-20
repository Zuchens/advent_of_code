import math
import re
from collections import Counter

import numpy as np
from numpy import rot90, array

with open("input1_example.txt") as f:
    raw_data = f.readlines()
    sc = []
    i = 0
    rows = []
    first = True
    while i < len(raw_data):
        raw_row = raw_data[i].strip()
        scanner_num = re.match("--- scanner (\d+) ---", raw_row)
        if scanner_num:
            number = int(scanner_num.group(1))

        elif raw_row == "":
            scanners = []
            if first == True:
                a = []
                for c in rows:
                    a.append([c[0], c[1],c[2]])
                scanners.append(a)
                first = False
            else:
                for rotation in [
                    [1,1,1],
                    [-1,1,1],
                    [1, -1, 1],
                    [1, 1, -1],
                    [-1, -1, 1],
                    [-1, 1, -1],
                    [1, -1, -1],
                    [-1, -1, -1]
                ]:
                    a = []
                    for c in rows:
                        a.append([rotation[0]*c[0],rotation[1]*c[1],rotation[2]*c[2]])
                    scanners.append(a)

                    a = []
                    for c in rows:
                        a.append([rotation[0]*c[0],rotation[1]*c[2],rotation[2]*c[1]])
                    scanners.append(a)

                    a = []
                    for c in rows:
                        a.append([rotation[0] * c[1], rotation[1] * c[0], rotation[2] * c[2]])
                    scanners.append(a)

                    a = []
                    for c in rows:
                        a.append([rotation[0] * c[1], rotation[1] * c[2], rotation[2] * c[0]])
                    scanners.append(a)

                    a = []
                    for c in rows:
                        a.append([rotation[0] * c[2], rotation[1] * c[0], rotation[2] * c[1]])
                    scanners.append(a)

                    a = []
                    for c in rows:
                        a.append([rotation[0] * c[2], rotation[1] * c[1], rotation[2] * c[0]])
                    scanners.append(a)
            sc.append(scanners)
            rows = []
        else:
            rows.append([int(x) for x in raw_row.split(",")])
        i += 1

list_vectors = []
for scanners in sc:
    vectors_per_scanner = []
    for row1 in scanners:
        vectors = dict()
        for i in range(len(row1)):
            for j in range(len(row1)):
                if i == j:
                    continue
                else:
                    element1=row1[i]
                    element2 = row1[j]
                    vectors[tuple([element1[0] - element2[0], element1[1] - element2[1], element1[2] -element2[2]])] = [element1,element2]

        vectors_per_scanner.append(vectors)
    list_vectors.append(vectors_per_scanner)
starting_points = [None for x in range(len(list_vectors))]
starting_points[0] = [0, 0, 0]
points = [set() for x in range(len(list_vectors))]
for p in sc[0][0]:
    points[0].add(tuple(p))
S = set()
# njsdvfo = [tuple([0,0,0]) for x in range(len(list_vectors))]
n = 11*12
all =list()
for idx1,vectors1 in enumerate(list_vectors):
    for idx2, vectors2 in enumerate(list_vectors):
        if starting_points[idx2] is not None:
            continue
        if vectors1 == vectors2:
            continue
        for i1, v1 in enumerate(vectors1):
            for i2, v2 in enumerate(vectors2):
                if len(set(v1.keys()).intersection(set(v2.keys())))>= n:
                    l1 = sc[idx1][i1]
                    l2 = sc[idx2][i2]
                    s = set()
                    for k1, v1e in v1.items():
                        if k1 in v2:
                            v2e = v2[k1]
                            s.add(tuple([v2e[1][0] + v1e[0][0],
                                         v2e[1][1] + v1e[0][1],
                                         v2e[1][2] + v1e[0][2]]))
                    if len(s) == 1:
                        mvniw = s.pop()
                        starting_point= tuple([-1*mvniw[0] + starting_points[idx1][0],
                                               -1*mvniw[1] + starting_points[idx1][1],
                                               -1*mvniw[2] + starting_points[idx1][2]])
                        S.add(starting_point)
                        list_vectors[idx2] = [v2]
                        starting_points[idx2] = starting_point

                        for v2e in set([tuple(x[0]) for x in v2.values()]):
                            a = (-1*(starting_points[idx2][0] + v2e[0]),
                                               -1*(starting_points[idx2][1] + v2e[1]),
                                               -1*(starting_points[idx2][2] + v2e[2]))
                            points[idx2].add(a)

                        a =1

print(starting_points)
all_counted = Counter([y for x in points for y in x])
print(len(all))
a = []
for k,v in sorted(all_counted.items(), key=lambda x:x[0]):
    if v >=2:
        print(k, v)
        a.append(k)
print(len(a))
