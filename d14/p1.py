import re
from collections import defaultdict, Counter
from copy import copy
from sys import maxsize


# with open("input1.txt") as f:
with open("input1.txt") as f:
    raw_data = f.readlines()
    template = raw_data[0].strip()
    template_list = []
    for idx in range(len(template)-1):
        template_list.append(f"{template[idx]}{template[idx+1]}")
    # if len(template) %2 != 0:
    template_list.append(f"{template[-1]}9")
    insertion_rules = {}
    for row in raw_data[2:]:
        elem1,elem2 =row.split("->")
        insertion_rules[elem1.strip()] = elem2.strip()
    a = 1
# while set(template_list).intersection(set(insertion_rules.keys())):
i = 0
n = 40
while i < n:
    print(i)
    idx = 0
    while idx < len(template_list):
        element = template_list[idx]
        if element in insertion_rules:
            replaced_str = insertion_rules[element]
            tmp1 = element[0] + replaced_str
            tmp2 = replaced_str + element[1]
            template_list[idx] = tmp1
            template_list.insert(idx+1, tmp2)
            idx+=1
        idx+=1
    i+=1

values = Counter([x[0] for x in template_list])
print(values.most_common()[0])
print(values.most_common()[-1])
print(values.most_common()[0][1] - values.most_common()[-1][1])