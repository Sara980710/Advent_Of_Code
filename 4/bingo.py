import os
import numpy as np

def check_board(board):
    sum_rows = np.sum(board, axis=0)
    sum_cols = np.sum(board, axis=1)

    win_rows = any(sum_rows == 5)
    win_cols = any(sum_cols == 5)

    return win_rows or win_cols
    

# Get input
current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('4/input.txt', 'r')
elif current_directory[-1:] == "2":
    file = open('input.txt', 'r')

input = file.readlines()

# Get number sequence
number_sequence = input[0].strip("\n").split(",")
number_sequence = np.array(number_sequence).astype(int)
print(f"{number_sequence =} ")

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
winner = None
for number in number_sequence:
    for player, boards in p_boards.items():
        board = boards[0].copy()
        track_board = boards[1]

        board = board == number

        track_board = track_board + board
        boards[1] = track_board

        win = check_board(track_board)

        if win:
            winner = player
            break

    if win:
        break

print(f"Winner is player {winner}")
print(f"board{p_boards[winner][0]}")


board = p_boards[winner][0]
track_board = p_boards[winner][1]

track_board = np.abs(track_board-1)

board = board*track_board

summation = sum(sum(board))

print(f"Score: {summation*number}")
