from collections import Counter

from tqdm import tqdm

horizontal = 0
depth = 0


def checks2(w, z, version, num1, num2):
    if version == 1:
        z = 26 * z + w + num1
    else:
        if (z - w - num1) % 26 == 0:
            z = (z - w - num1) // 26
        else:
            z = z // 26 * 26 + w + num2
    return z


def checks(inputs, number_input, z):
    data = {"x": 0, "y": 0, "z": z, "w": 0}
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
                data[elements[1]] %= elements2

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
            i += 1
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
        100,
        2000,
        20000,
        600000,  # ?
        50000,
        600000,  # ?
        50000,
        20000,
        20000,
        20000,
        20000,
        20000,
        20000,
        30000,
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
        (1, 0, -1),
        (1, 6, -1),
        (1, 4, -1),
        (1, 2, -1),
        (1, 9, -1),
        (2, 2, 1),
        (1, 10, -1),
        (2, 15, 6),
        (2, 10, 4),
        (1, 6, -1),
        (2, 10, 3),
        (2, 4, 9),
        (2, 1, 15),
        (2, 1, 5),
    ]
    z_res = [0]

    found = False
    map = {}

    # numbers = [9,4,9,9,2,9,9,4,1,9,5,9,9,8]
    # checker = [9,9,4,9,9,2,9,9,4,1,9,5,9,9]
    def function(w0, z0=0, depth=0):
        global found
        global map
        if found:
            return ""
        if (w0, z0, depth) in map:
            return map[(w0, z0, depth)]
        calc = calulated[depth]
        answer = checks2(w0, z0, calc[0], calc[1], calc[2])
        # answer = checks(parts[depth], w0, z0)
        if depth == 13:
            if answer == 0:
                found = True
                return f"00"
            else:
                return f"0"

        values = []
        for i in range(1, 10, 1):
            value = f"{i}{function(i, answer, depth + 1)}"
            values.append(value)
        max_size= max([len(x) for x in values])
        values_sizes = [x for x in values if len(x) == max_size]
        values = sorted(values_sizes)
        one_value = values[-1]
        map[(w0, z0, depth)] = one_value
        return one_value


    datas = []
    for i in range(1, 10, 1):
        datas.append(f"{i}{function(i)}")
    print(datas)

    # new_s = []
    # for i in data:
    #     new_s.append(max([j[2] for j in i]))
    # print(new_s)
    # a = 1
