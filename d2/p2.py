horizontal = 0
depth = 0
aim = 0
with open("input1.txt") as f:
    for row in f.readlines():
        elements = row.split(" ")
        name = elements[0]
        number = int(elements[1])
        if name == "forward":
            horizontal+=number
            depth += aim*number
        elif name == "down":
            aim+=number
        elif name == "up":
            aim-=number

print(horizontal*depth)
