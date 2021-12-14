from collections import defaultdict
from copy import copy

with open("input1.txt") as f:
    raw_data = f.readlines()
    data = defaultdict(list)
    for raw_row in raw_data:
        start, end = raw_row.strip().split("-")
        data[start].append(end)
        data[end].append(start)


def f(name, prev_path):
    if name == "end":
        return [prev_path]
    current_path = []
    for i in data[name]:
        if i == "start":
            continue
        if i.islower() and i in prev_path:
            a = [x for x in prev_path if x.islower()]
            if len(a) != len(set(a)):
                continue
        path = copy(prev_path)
        path.append(i)
        paths = f(i, path)
        current_path.extend(paths)
    return current_path


paths = f("start", ["start"])
d = []
for i in paths:
    if i:
        d.append(i)
        print(",".join(i))
print(len(d))
