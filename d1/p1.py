with open("input1.txt") as f:
    data = f.readlines()
prev = 0
it = 0
for idx, v in enumerate(data):
    v = int(v)
    if idx == 0:
        prev = v
        continue
    else:
        if prev < v:
            it += 1
        prev = v
print(it)
