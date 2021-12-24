import re
from copy import copy
from dataclasses import dataclass

from tqdm import tqdm
# 27075190051476
# 27075190051476
# 444356092776315
# 2140974489582
# 57806311218714
with open("input1_example.txt") as f:
    data = f.read()
    match1_raw = re.findall("Player 1 starting position: (\d)", data)

    match2_raw = re.findall("Player 2 starting position: (\d)", data)

N = 4
# values = [0 for i in range(30)]
default_position1 = int(match1_raw[0])
default_position2 = int(match2_raw[0])
possibilities  = [0,0,0,1,3,6,7,6,3,1]
# possibilities  = [2]
#
def get_rolls(available_positions, data, worlds, data2):
    won =0
    not_won = 0
    won2 = 0
    new_positions = set()
    new_data = [[0 for positions in range(11)] for points in range(N)]
    all_possibilities = 0
    while available_positions:
        default_position, points, current_possibilities = available_positions.pop()
        if data[points][default_position] !=0:
            current_possibilities = data[points][default_position]
        for roll, roll_possibilities in enumerate(possibilities):
            all_possibilities+=roll_possibilities
            if roll_possibilities == 0:
                continue
            if (default_position + roll) % 10 == 0:
                position = 10
            else:
                position = (default_position + roll) % 10
            if points + position >= N:
                won += current_possibilities * roll_possibilities*worlds

            else:
                new_data[points + position][position] += current_possibilities * roll_possibilities
                not_won += current_possibilities * roll_possibilities *worlds
                new_positions.add((position, points + position, new_data[points + position][position]))

    for i in range(len(new_data)):
        for j in range(len(new_data[i])):
            new_data[i][j] = new_data[i][j] * worlds

    for i in range(len(data2)):
        for j in range(len(data2[i])):
            data2[i][j] = data2[i][j] * not_won


            # if won > 0 and data2[i][j] > 0:
            #     data2[i][j] = data2[i][j] - won


    print(not_won, won)
    a = 1
    for i in new_data:
        for j in i:
            print(f"{j:8d}", end="")
        print()
    print()

    for i in data2:
        for j in i:
            print(f"{j:8d}", end="")
        print()
    print()

    if sum([i for x in data2 for i in x]) !=0:
        d = sum([i for x in new_data for i in x])
        e = sum([i for x in data2 for i in x])
        print(d,e)
        assert d ==e
    # for i in range(len(new_data)):
    #     for j in range(len(new_data[i])):
    #         new_data[i][j]=new_data[i][j]*worlds

    return new_positions,new_data, won, not_won

all_won = 0
all_won2 = 0
worlds = 1
available_positions = {(default_position1, 0, 1)}
data = [[0 for positions in range(11)] for points in range(N)]
available_positions2 = {(default_position2, 0, 1)}
data2 = [[0 for positions in range(11)] for points in range(N)]
prev_won = 0
while True:

    available_positions, data, won, worlds = get_rolls(available_positions, data, worlds, data2)
    all_won+=won
    if len(available_positions)==0:
        break
    # print(won, worlds)
    available_positions2, data2, won2, worlds = get_rolls(available_positions2, data2, worlds, data)
    all_won2 += won2
    # print(won2, worlds)
    if len(available_positions2) == 0:
        break
    # print("u1")
    # for i in data:
    #     for j in i:
    #         print(f"{j:8d}", end="")
    #     print()
    # print()
    #
    # print("u2")
    # for i in data2:
    #     for j in i:
    #         print(f"{j:8d}", end="")
    #     print()
    # print()

if all_won > all_won2:
    print(all_won)
else:
    print(all_won2)


print(all_won)
print(all_won2)





