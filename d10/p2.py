import sys
from copy import copy

points = {")":3, "]":57, "}":1197, ">":25137}
closes = {"(":1, "[":2, "{": 3, "<": 4}
all_closing = []
with open("input1.txt") as f:
    data = f.readlines()
    new_data = copy(data)
    calulated = 0
    for row in data:
        taken = []
        for idx, element in enumerate(row.strip()):
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
            if idx == len(row.strip())-1:
                closing_points = 0
                taken.reverse()
                for closing in taken:
                    closing_points = 5*closing_points +closes[closing]
                all_closing.append(closing_points)
                a = 1
all_closing = sorted(all_closing)
print(all_closing[int(len(all_closing)/2)])





