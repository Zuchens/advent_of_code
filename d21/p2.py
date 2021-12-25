import re
from collections import defaultdict

with open("input1.txt") as f:
    data = f.read()
    match1_raw = re.findall("Player 1 starting position: (\d)", data)

    match2_raw = re.findall("Player 2 starting position: (\d)", data)

N = 21
default_position1 = int(match1_raw[0])
default_position2 = int(match2_raw[0])
possibilities  = [0,0,0,1,3,6,7,6,3,1]

def get_rolls(available_positions, worlds, won1, won2):
    print(f"Worlds: {worlds}")
    not_won = 0
    new_positions = defaultdict(int)
    for key, current_possibilities in available_positions.items():
        player1, player2 = key
        default_position1, points1 = player1
        for roll1, roll_possibilities1 in enumerate(possibilities):
            if roll_possibilities1 == 0:
                continue
            if (default_position1 + roll1) % 10 == 0:
                position1 = 10
            else:
                position1 = (default_position1 + roll1) % 10
            if points1 + position1 >= N:
                won1 += current_possibilities * roll_possibilities1
            else:
                default_position2, points2 = player2
                for roll2, roll_possibilities2 in enumerate(possibilities):
                    if roll_possibilities2 == 0:
                        continue
                    if (default_position2 + roll2) % 10 == 0:
                        position2 = 10
                    else:
                        position2 = (default_position2 + roll2) % 10
                    if points2 + position2 >= N:
                        won2 += current_possibilities * roll_possibilities2 * roll_possibilities1
                    else:
                        not_won +=current_possibilities * roll_possibilities1*roll_possibilities2
                        new_positions[(position1, points1 + position1), (position2, points2 + position2)] += current_possibilities * roll_possibilities1*roll_possibilities2



    return new_positions, won1, won2, not_won

won1 = 0
won2 =0
worlds = 1
available_positions = {((default_position1, 0),(default_position2, 0)):1}

prev_won = 0
while True:

    available_positions, won1, won2,worlds = get_rolls(available_positions, worlds, won1, won2)
    print(f"Current roll won1 {won1}, won2: {won2} not won {worlds}")
    if len(available_positions)==0:
        break


if won1 > won2:
    print(won1)
else:
    print(won2)
