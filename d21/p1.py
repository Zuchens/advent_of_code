import re
from dataclasses import dataclass

from tqdm import tqdm

@dataclass
class Player:
    position: int
    points: int = 0

    def add(self, roll):
        if (self.position + roll)%10 == 0:
            position = 10
        else:
            position = (self.position+roll)%10
        self.position = position
        self.points+=self.position

class Dice:
    number: int = 0

def roll(dice):
    if dice.number >=100:
        dice.number = 0
    dice.number +=1
    return dice.number



with open("input1_example.txt") as f:
    data = f.read()
    match1_raw = re.findall("Player 1 starting position: (\d)", data)
    player1 = Player(int(match1_raw[0]))

    match2_raw = re.findall("Player 2 starting position: (\d)", data)
    player2 = Player(int(match2_raw[0]))
rolled = 0
dice = Dice()

while True:
    values = [roll(dice),roll(dice),roll(dice)]
    value  = sum(values)
    player1.add(value)
    rolled+=3
    if player1.points >= 1000:
        break
    print(f"Player1 {player1.position} {player1.points} {values}")
    values = [roll(dice), roll(dice), roll(dice)]
    value  = sum(values)
    player2.add(value)
    rolled += 3
    if player2.points >= 1000:
        break
    print(f"Player2 {player2.position} {player2.points} {values}")

if player1.points < player2.points:
    print(player1.points*rolled)
else:
    print(player2.points * rolled)





