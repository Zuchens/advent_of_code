from sys import maxsize

from tqdm import tqdm

with open("input1.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

maxvalue = 0
for i in data:
    if maxvalue < i:
        maxvalue = i

minsum = maxsize
for i in tqdm(range(maxvalue)):
    value = sum([sum([j for j in range(abs(elem - i)+1)]) for elem in data])
    if minsum > value:
        minsum = value

print(minsum)



