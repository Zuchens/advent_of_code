from copy import copy

with open("input1.txt") as f:
    data = [x.strip() for x in f.readlines()]

data1 = copy(data)
for i in range(len(data1[0])):
    # values = [0 for _ in range(len(data[0]))]
    values = 0
    for row in data1:
        values = values + int(row[i])
    if values > len(data1) / 2.:
        o = 1
    elif values == len(data1) / 2.:
        o = 1
    else:
        o = 0
    oxygen_gen = [x for x in data1 if int(x[i]) == o]
    data1 = oxygen_gen

data2 = copy(data)
for i in range(len(data2[0])):
    values = 0
    for row in data2:
        values = values + int(row[i])
    # co2 = 0 if values > len(data2)/2 else 1
    if values < len(data2) / 2.:
        co2 = 1
    elif values == len(data2) / 2.:
        co2 = 0
    else:
        co2 = 0
    co2_gen = [x for x in data2 if int(x[i]) == co2]
    data2 = co2_gen
    if len(data2) == 1:
        break

print(int(data1[0], 2), int(data2[0], 2), int(data1[0], 2) * int(data2[0], 2))
