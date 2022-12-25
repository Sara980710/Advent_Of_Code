import os
import numpy as np
from numpy.lib.index_tricks import AxisConcatenator

def check_board(board):
    sum_rows = np.sum(board, axis=0)
    sum_cols = np.sum(board, axis=1)

    win_rows = any(sum_rows == 5)
    win_cols = any(sum_cols == 5)

    return win_rows or win_cols
    

# Get input
current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('4/gidde.txt', 'r')
elif current_directory[-1:] == "2":
    file = open('input.txt', 'r')

input = file.readlines()

# Get number sequence
number_sequence = input[0].strip("\n").split(",")
number_sequence = np.array(number_sequence).astype(int)

# Get player boards
p_boards = {}
player = 0
board = np.zeros([5, 5])
row=0

for line in input[1:]:
    
    row_numbers = line.split(" ")
    if "\n" in row_numbers:
        continue

    row_numbers[-1] = row_numbers[-1].strip("\n")

    board[row, :] = [int(c) for c in row_numbers if not c == '']
    row += 1

    if row==5:
        p_boards[player] = [board.copy(), np.zeros([5, 5])]
        player +=1
        row = 0

# Begin bingo
all_won = False
players_left = list(p_boards.keys())
for number in number_sequence:
    bingo = []
    for player in players_left:
        boards = p_boards[player]
        board = boards[0].copy()
        track_board = boards[1]

        board = board == number

        track_board = track_board + board
        boards[1] = track_board

        win = check_board(track_board)

        if win:
            bingo.append(player)
        
    for player in bingo:
        players_left.pop(players_left.index(player))

        if len(players_left) == 1:
            winner = players_left[0]
        elif len(players_left) == 0:
            all_won = True
            break

    if all_won:
        break

print(f"Winner is player {winner}")
print(f"board{p_boards[winner][0]}")


board = p_boards[winner][0]
track_board = p_boards[winner][1]

track_board = np.abs(track_board-1)

board = board*track_board

summation = sum(sum(board))

print(f"Score: {summation*number}")
