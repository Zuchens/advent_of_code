with open("input1.txt") as f:
    raw_algorithm, raw_image = f.read().split("\n\n")
    algorithm = [1 if element == "#" else 0 for element in raw_algorithm.strip()]

    image = []
    for row in raw_image.strip().split("\n"):
        image.append([1 if element == "#" else 0 for element in row])
inf = 0
idx = 0
while idx < 50:
    image2 = []
    N = 1
    for i in range(N):
        image2.append([inf for x in range(len(image[0]) + N*2)])
    for i in range(len(image)):
        row = []
        row.extend([inf] * N)
        for j in range(len(image[0])):
            row.append(image[i][j])
        row.extend([inf] * N)
        image2.append(row)
    for i in range(N):
        image2.append([inf for x in range(len(image[0]) + N*2)])
    image = image2

    output_image = [[-1 for _ in range(len(image[0]))] for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            str_value = ""

            for k, v in [(-1, -1), (-1, 0), (-1, 1),
                         (0, -1), (0, 0), (0, 1),
                         (1, -1), (1, 0), (1, 1)]:
                i1 = i + k
                j1 = j + v
                if i1 >= 0 and i1 < len(image) and j1 >= 0 and j1 < len(image):
                    tmp = image[i + k][j + v]
                else:
                    tmp = inf
                str_value += str(tmp)
            value = int(str_value, 2)
            output_image[i][j] = algorithm[value]
    lit = 0
    for i in range(len(output_image)):
        for j in range(len(output_image[0])):
            if output_image[i][j] == 1:
                lit += 1
    idx += 1
    image = output_image
    if inf == 0:
        inf = algorithm[0]
    else:
        inf = algorithm[-1]
print(lit)