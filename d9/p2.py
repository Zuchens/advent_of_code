import sys


with open("input1.txt") as f:
    data = f.readlines()
    parsed_data = []
    parsed_row = [sys.maxsize]
    parsed_row.extend([sys.maxsize for _ in data[0].strip()])
    parsed_row.extend([sys.maxsize])
    parsed_data.append(parsed_row)

    for row in data:
        parsed_row = [sys.maxsize]
        parsed_row.extend([int(i) for i in row.strip()])
        parsed_row.extend([sys.maxsize])
        parsed_data.append(parsed_row)

    parsed_row = [sys.maxsize]
    parsed_row.extend([sys.maxsize for i in data[0].strip()])
    parsed_row.extend([sys.maxsize])
    parsed_data.append(parsed_row)

points = []
l = []
for i in range(1, len(parsed_data)-1):
    for j in range(1, len(parsed_data[0])-1):
        good = True
        for k,v in [(-1,0), (0, -1), (0,1),(1,0)]:
            if k ==0 and v == 0:
                continue
            else:
                if parsed_data[i+k][j+v] <= parsed_data[i][j]:
                    good = False

        if good:
            points.append(parsed_data[i][j]+1)
            l.append(tuple([i,j]))

print(sum(points))
sizes = []
for i,j in l:
    elem = tuple([i,j])
    stack = [elem]
    already_seen = set([elem])
    size = 0
    while stack:
        elem = stack[0]
        stack.remove(elem)
        size+=1
        for k, v in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if parsed_data[elem[0] + k][elem[1] + v] < 9 and tuple([elem[0] + k, elem[1] + v]) not in already_seen:
                stack.append(tuple([elem[0] + k, elem[1] + v]))
                already_seen.add(tuple([elem[0] + k, elem[1] + v]))
    sizes.append(size)

a = sorted(sizes, reverse=True)[:3]
b = a[0]*a[1]*a[2]
print(b)
print(a)





