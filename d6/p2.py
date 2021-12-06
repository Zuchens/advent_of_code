#### TASK 1

with open("input1.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]

elements = {i: 0 for i in range(9)}
for element in data:
    elements[element]+=1
for j in range(256):
    new_elements = {}
    new = 0
    for key in elements.keys():
        if key != 7:
            if key > 0:
                new_elements[key-1] = elements[key]
            else:
                new_elements[6] = elements[0] + elements[7]
                new_elements[8] = elements[0]
    elements = new_elements
print(sum(list(elements.values())))