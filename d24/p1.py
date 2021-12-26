from collections import Counter

from tqdm import tqdm

horizontal = 0
depth = 0


def checks2(version,z, w, num1, num2):
    if version ==1:
        z = 26*z+w+num1
    else:
        if (z-w-num1)%26 ==0:
            z = (z-w-num1)%26
        else:
            z = z//26*26+w+num2
    return z

def checks(data, inputs, number_input):

    for elements in inputs:
        if len(elements) == 2 and elements[0] == "inp":
            data[elements[1]] = number_input
        else:
            elements2 = data[elements[2]] if elements[2] in data else int(elements[2])
            if elements[0] == "add":
                data[elements[1]] += elements2
            elif elements[0] == "mul":
                data[elements[1]] *= elements2
            elif elements[0] == "div":
                data[elements[1]] /= elements2
                data[elements[1]] = int(data[elements[1]])

            elif elements[0] == "mod":
                data[elements[1]]%=  elements2

            elif elements[0] == "eql":
                data[elements[1]] = data[elements[1]] == elements2
                data[elements[1]] = 1 if data[elements[1]] is True else 0
            else:
                print("brrrr")
    return data["z"]


with open("input1.txt") as f:
    lines = []
    for row in f.readlines():
        parsed_row = row.strip()
        elements = parsed_row.split(" ")
        lines.append(elements)

    parts = []
    i = 0
    while i < len(lines):
        not_imp = []
        if lines[i] and "w" in lines[i]:
            not_imp.append(lines[i])
            i+=1
            while i < len(lines) and not ("inp" in lines[i] and "w" in lines[i]):
                not_imp.append(lines[i])
                i += 1
            parts.append(not_imp)
    data = [[] for i in range(14)]

    z_placeholders = range(100000)
    # z_placeholders
    # z_ranges2 = [
    #     100,
    #     2000,
    #     20000,
    #     600000,  #?
    #     50000,
    #     600000, #?
    #     50000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     30000,
    # ]
    # z_ranges2 = [
    #     100,
    #     2000,
    #     20000,
    #     600000,  #?
    #     50000,
    #     600000, #?
    #     50000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     20000,
    #     30000,
    # ]

    z_ranges2 = [
        1000,
        20000,
        200000,
        600000,  #?
        500000,
        600000, #?
        500000,
        200000,
        200000,
        200000,
        200000,
        200000,
        200000,
        300000,
    ]
    # z_ranges2 = [
    #     100,
    #     2000,
    #     40000,
    #     400000,  #?
    #     400000,
    #     400000, #?
    #     400000,
    #     400000,
    #     400000,
    #     400000,
    #     400000,
    #     400000,
    #     400000,
    #     400000,
    #
    # ]


    calulated = [
        (1,0,-1),
        (1,6,-1),
        (1,5,-1),
        (1, 2, -1),
        (1, 9, -1),
        (2, 2, 1),
        (1, 10, -1),
        (2, 15, 6),
        (2, 10, 4),
        (1, 6, -1),
        (2, 10, 3),
        (2, 3, 9),
        (2, 1, 15),
        (2, 1, 5),
    ]

    z_res = [0]

    z =0
    for idx, part in enumerate(zip(parts,numbers)):
        part, w = part
        new_z_placeholders = []
        checked = checks({"z": z, "w": 0, "x": 0, "y": 0}, part, w)
        print(checked, z, w)
        z = checked
        # print(13 - idx, z_res[-1], z_res[0])

#99499299419599
#94992994195998

    # new_s = []
    # for i in data:
    #     new_s.append(max([j[2] for j in i]))
    # print(new_s)
    # a = 1
