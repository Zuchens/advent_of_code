import re
from collections import defaultdict, Counter
from copy import copy
from sys import maxsize



with open("input1.txt") as f:
    raw_data = f.readlines()
    template = raw_data[0].strip()
    template_list = defaultdict(int)
    for idx in range(len(template)-1):
        template_list[f"{template[idx]}{template[idx+1]}"]+=1
    template_list[f"{template[-1]}9"]+=1
    insertion_rules = {}
    for row in raw_data[2:]:
        elem1,elem2 =row.split("->")
        insertion_rules[elem1.strip()] = elem2.strip()
    a = 1
i = 0
n = 40
print(template_list)
while i < n:
    tmp_list_cp = defaultdict(int)
    tmp = copy(list(template_list.items()))
    for element,value in tmp:
        if element in insertion_rules and value > 0:
            replaced_str = insertion_rules[element]
            tmp1 = element[0] + replaced_str
            tmp2 = replaced_str + element[1]
            tmp_list_cp[tmp1]+=value
            tmp_list_cp[tmp2]+= value
    for key, value in tmp:
        if key not in tmp_list_cp and key not in insertion_rules:
            tmp_list_cp[key] = value
    i+=1
template_list = tmp_list_cp
chars = defaultdict(int)
for element,value in template_list.items():
    chars[element[0]]+=value

sort = sorted(chars.items(),key=lambda x: x[1])
print(sort[-1][1] - sort[0][1])
