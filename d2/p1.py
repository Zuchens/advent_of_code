horizontal = 0
depth = 0
with open("input1.txt") as f:
    for row in f.readlines():
        elements = row.split(" ")
        name = elements[0]
        number = int(elements[1])
        if name == "forward":
            horizontal+=number
        elif name == "down":
            depth+=number
        elif name == "up":
            depth-=number

print(horizontal*depth)
