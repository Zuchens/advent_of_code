
from tqdm import tqdm

with open("input1.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

for j in tqdm(range(256)):
    i = 0
    while(i < len(data)):
        element_value = data[i]
        if element_value > 0:
            data[i]=element_value-1
        else:
            data[i] = 6
            data.append(9)
        i+=1
print(len(data))