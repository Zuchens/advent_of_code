import re
from collections import defaultdict, Counter
from copy import copy
from sys import maxsize

import time

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}
bin2hex = {v: k for k, v in hex2bin.items()}
start_time = time.time()

version_sum = 0
def fun(data):
    global version_sum
    version_bin = f"{int(data[:3]):04d}"
    version_hex = bin2hex[version_bin]
    type_id_bin = f"{int(data[3:6]):04d}"
    type_id_hex = bin2hex[type_id_bin]
    rest_data = data[6:]
    print(version_hex, type_id_hex, data)
    version_sum = version_sum+int(version_bin, 2)
    if type_id_hex == '4':
        i = 0
        groups = []
        while True:
            if rest_data[i] == "1":
                groups.append(rest_data[i + 1:i + 5])
                i = i + 5
            else:
                groups.append(rest_data[i + 1:i + 5])
                i = i + 5
                break

        value = int("".join(groups), 2)
        return value, rest_data[i:]
    else:
        length_type_id = rest_data[0]
        rest_data = rest_data[1:]
        if length_type_id == '0':
            length_of_subpackets = int(rest_data[:15], 2)
            rest_data, what_is_left = rest_data[15:length_of_subpackets + 15], rest_data[length_of_subpackets + 15:]
            values = []
            while rest_data:
                value, rest_data = fun(rest_data)
                values.append(value)
            return sum(values), what_is_left
        else:
            number_of_packages = int(rest_data[:11], 2)
            rest_data = rest_data[11:]
            values = []
            for i in range(number_of_packages):
                value, rest_data = fun(rest_data)
                values.append(value)
            return sum(values), rest_data


with open("input1_example.txt") as f:
    raw_data = f.read().strip()
    processing_data = []
    for i in raw_data:
        processing_data.append(hex2bin[i])
    data = "".join(processing_data)
b = fun(data)
# a = 1
# print(b)
print(version_sum)

print("--- %s seconds ---" % (time.time() - start_time))
