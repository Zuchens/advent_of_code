#### TASK 2
from dataclasses import dataclass
from typing import List

@dataclass
class Row:
    sum: int
    marked: int
@dataclass
class Board:
    board_data: List[List[int]]
    horizontal: List[Row]
    vertical: List[Row]

def bingo(draw, boards):
    available_boards = set(range(len(boards)))
    for draw_element in draw:
        for idx, board in enumerate(boards):
           for i in range(len(board.board_data)):
               for j in range(len(board.board_data[i])):
                   board_element = board.board_data[i][j]
                   if idx in available_boards and draw_element == board_element:
                        print(draw_element,idx, i, j)
                        board.horizontal[i].sum -= board_element
                        board.horizontal[i].marked+=1
                        board.vertical[j].sum -=board_element
                        board.vertical[j].marked += 1
                        if board.vertical[j].marked == 5 or board.horizontal[i].marked == 5:
                            if len(available_boards) == 1:
                                return board, draw_element
                            available_boards.remove(idx)



def process(data):
    boards = []
    board_data = []
    horizontal = []
    vertical = []
    for i in range(len(data)-2):
        row = data[i+2].strip()
        if row == "":
            boards.append(Board(board_data, horizontal,vertical))
            board_data = []
            horizontal = []
            vertical = []
        else:
            parsed_row = []
            for element in row.split(" "):
                if element.strip() =="":
                    continue
                parsed_row.append(int(element))
            board_data.append(parsed_row)
            horizontal.append(Row(0,0))
            vertical.append(Row(0,0))
    boards.append(Board(board_data, horizontal,vertical))
    return boards

def group(boards):
    for board in boards:
        for i in range(len(board.board_data)):
            for j in range(len(board.board_data[i])):
                board.horizontal[i].sum+=board.board_data[i][j]

        for i in range(len(board.board_data)):
            for j in range(len(board.board_data[i])):
                board.vertical[i].sum+=board.board_data[j][i]


with open("input1.txt") as f:
    data = [ x.strip() for x in f.readlines()]
draw = [int(x.strip()) for x in data[0].split(",")]

boards = process(data)
group(boards)
board, draw_element = bingo(draw, boards)
unmarked = sum([x.sum for x in board.horizontal])
print(unmarked,draw_element, unmarked*draw_element)