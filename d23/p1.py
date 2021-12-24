with open("input1.txt") as f:
    data = [x.strip() for x in f.readlines()]
    max_x  = 13
    max_y = 5
    processed_data = [["" for i in range(max_x)] for j in range(max_y)]
    processed_data[3][0] = "o"
    processed_data[4][0] = "o"
    processed_data[3][1] = "o"
    processed_data[4][1] = "o"

    processed_data[3][-1] = "o"
    processed_data[4][-1] = "o"
    processed_data[3][-2] = "o"
    processed_data[4][-2] = "o"

    elements = {"A":[],"B": [],"C": [], "D":[]}

    for i in range(max_y):
        k = 0
        for j in range(max_x):
            if processed_data[i][j] != "o":
                processed_data[i][j] = data[i][k]
                if data[i][k] in {"A", "B","C","D"}:
                    elements[data[i][k]].append((i,j))
                k+=1

    expected = {"A":[(2,3)(3,3)],"B":[(2,5)(3,5)],"C":[(2,7)(3,7)],"D":[(2,9)(3,9)]}

    while elements != expected:


    for i in processed_data:
        print("".join(i))

    a = 1

