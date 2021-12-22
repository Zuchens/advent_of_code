import re
from copy import copy
from dataclasses import dataclass

from tqdm import tqdm


with open("input1_example.txt") as f:
    data = f.read()
    match1_raw = re.findall("Player 1 starting position: (\d)", data)

    match2_raw = re.findall("Player 2 starting position: (\d)", data)

N = 21

# values = [0 for i in range(30)]
default_position1 = int(match1_raw[0])
default_position2 = int(match2_raw[0])
possibilities  = [0,0,0,1,3,6,7,6,3,1]


def get_rolls(available_positions, data):
    won =0
    new_positions = set()
    new_data = [[0 for positions in range(11)] for points in range(N)]
    while available_positions:
        default_position, points, current_possibilities = available_positions.pop()
        for roll, roll_possibilities in enumerate(possibilities):
            if roll_possibilities == 0:
                continue
            if (default_position + roll) % 10 == 0:
                position = 10
            else:
                position = (default_position + roll) % 10
            if points + position >= N:
                won += current_possibilities * roll_possibilities
            else:
                new_data[points + position][position] += current_possibilities * roll_possibilities
                new_positions.add((position, points + position, new_data[points + position][position]))

    return new_positions,new_data, won

all_won = 0
data = [[0 for positions in range(11)] for points in range(N)]
available_positions = {(default_position1, 0, 1)}
while True:
    available_positions = {(default_position1, 0, 1)}
    data = [[0 for positions in range(11)] for points in range(N)]
    available_positions, data, won = get_rolls(available_positions, data)
    all_won+=won

    for i in data:
        for j in i:
            print(f"{j:3d}",end="")
        print()
    print()
    a =1
    # available_positions2 = {(default_position2, 0, 1)}
    # data2 = [[0 for positions in range(11)] for points in range(N)]
    # available_positions2, data2, won2 = get_rolls(available_positions2, data2)
    # all_won += won

if player1.points < player2.points:
    print(player1.points*rolled)
else:
    print(player2.points * rolled)





