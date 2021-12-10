from sys import maxsize

from tqdm import tqdm
info = {
0:{"a","b","c",    "e","f","g"},
1:{        "c",        "f"    },
2:{"a",    "c","d","e",    "g"},
3:{"a",    "c","d",    "f","g"},
4:{    "b","c","d",    "f"    },
5:{"a","b",    "d",    "f","g"},
6:{"a","b",    "d","e","f","g"},
7:{"a",    "c",        "f"    },
8:{"a","b","c","d","e","f","g"},
9:{"a","b","c","d",    "f","g"},
}

"""
    0: {"a", "b", "c", "e", "f", "g"}, 6
    1: {"c", "f"}, 2
    2: {"a", "c", "d", "e", "g"}, 5
    3: {"a", "c", "d", "f", "g"}, 5
    4: {"b", "c", "d", "f"}, 4
    5: {"a", "b", "d", "f", "g"}, 5
    6: {"a", "b", "d", "e", "f", "g"}, 6
    7: {"a", "c", "f"}, 3
    8: {"a", "b", "c", "d", "e", "f", "g"}, 7
    9: {"a", "b", "c", "d", "f", "g"}, 6
"""
with open("input1.txt") as f:
    data = f.readlines()
parsed_input =[]
parsed_output =[]
for row in data:
    input, output = row.split("|")
    input = [x.strip() for x in input.strip().split(" ")]
    parsed_input.append(input)
    output = [x.strip() for x in output.strip().split(" ")]
    parsed_output.append(output)

values = 0
for i in parsed_output:
    for number in i:
        if len(number) in {2,3,4,7}:
            values+=1
print(values)