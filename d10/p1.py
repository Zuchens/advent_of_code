import sys
points = {")":3, "]":57, "}":1197, ">":25137}


with open("input1.txt") as f:
    data = f.readlines()
    calulated = 0
    for row in data:
        taken = []
        for element in row.strip():
            if element in "{[<(":
                taken.append(element)
            else:
                if taken[-1] == "{" and element !="}" :
                    calulated+=points[element]
                    break
                if taken[-1] == "<" and element !=">" :
                    calulated+=points[element]
                    break
                if taken[-1] == "[" and element !="]" :
                    calulated+=points[element]
                    break
                if taken[-1] == "(" and element !=")" :
                    calulated+=points[element]
                    break
                taken.pop()
    print(calulated)
    a = 1





