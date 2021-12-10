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

print(sum(points))



