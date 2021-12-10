import itertools
from collections import Counter
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
info2 = {
"".join(["a","b","c",    "e","f","g"]),
"".join([        "c",        "f"    ]),
"".join(["a",    "c","d","e",    "g"]),
"".join(["a",    "c","d",    "f","g"]),
"".join([    "b","c","d",    "f"    ]),
"".join(["a","b",    "d",    "f","g"]),
"".join(["a","b",    "d","e","f","g"]),
"".join(["a",    "c",        "f"    ]),
"".join(["a","b","c","d","e","f","g"]),
"".join(["a","b","c","d",    "f","g"]),
}
info3 = {
"".join(["a","b","c",    "e","f","g"]):"0",
"".join([        "c",        "f"    ]):"1",
"".join(["a",    "c","d","e",    "g"]):"2",
"".join(["a",    "c","d",    "f","g"]):"3",
"".join([    "b","c","d",    "f"    ]):"4",
"".join(["a","b",    "d",    "f","g"]):"5",
"".join(["a","b",    "d","e","f","g"]):"6",
"".join(["a",    "c",        "f"    ]):"7",
"".join(["a","b","c","d","e","f","g"]):"8",
"".join(["a","b","c","d",    "f","g"]):"9",
}
abc= tuple(["a", "b", "c", "d", "e", "f", "g"])
with open("input1.txt") as f:
    data = f.readlines()
parsed_input =[]
parsed_output =[]
for row in data:
    input, output = row.split("|")
    input = ["".join(sorted(x.strip())) for x in input.strip().split(" ")]
    parsed_input.append(input)
    output = ["".join(sorted(x.strip())) for x in output.strip().split(" ")]
    parsed_output.append(output)


values = 0
good_combinations = []
for input in parsed_input:
    possibilities = {}
    for element in input:
        if len(element) == 2:
            possibilities[element[0]] = {"c","f"}
            possibilities[element[1]] = {"c", "f"}
    for element in input:
        if len(element) == 3:
            for char in element:
                if char not in possibilities:
                    possibilities[char] = {"a"}
    for element in input:
        if len(element) == 4:
            for char in element:
                if char not in possibilities:
                    possibilities[char] = {"b", "d"}
    for alphabet in abc:
        if alphabet not in possibilities:
            possibilities[alphabet] = {"e","g"}
    combination = list(itertools.product(possibilities["a"],
                           possibilities["b"],
                           possibilities["c"],
                           possibilities["d"],
                           possibilities["e"],
                           possibilities["f"],
                           possibilities["g"]))
    good_combination = []
    new_comb = []
    for c in combination:
        if Counter(c).most_common()[0][1] != 1:
            continue
        new_comb.append(c)
    for c in new_comb:
        map = {key: value for key, value in zip(abc, c)}
        good_combination = map
        for element in input:
            new_el = []
            for i in set(element):
                new_el.append(map[i])
            n =  "".join(sorted(new_el))
            if n not in info2:
                good_combination = {}
                break
        if good_combination:
            good_combinations.append(good_combination)
            break
numbers = []
for idx,j in enumerate(parsed_output):
    digits = []
    for element in j:
        new_el = []
        for i in element:
            new_el.append(good_combinations[idx][i])
        n = "".join(sorted(new_el))
        digits.append(info3[n])
    numbers.append(int("".join(digits)))
    # print(numbers)



print(sum(numbers))