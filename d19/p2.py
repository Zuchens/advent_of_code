with open("input1.txt") as f:
    data = f.readlines()
data = [int(x) for x in data]
prev = 0
it = 0
sums = []
for idx in range(len(data)):
    value = data[idx]
    if idx + 1 < len(data):
        value += data[idx + 1]
    if idx + 2 < len(data):
        value += data[idx + 2]
    sums.append(value)

for idx, v in enumerate(sums):
    if idx == 0:
        prev = v
        continue
    else:
        if prev < v:
            it += 1
        prev = v
print(it)

