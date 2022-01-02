import os
import numpy as np
from matplotlib import pyplot as plt

def check_board(board):
    sum_rows = np.sum(board, axis=0)
    sum_cols = np.sum(board, axis=1)

    win_rows = any(sum_rows == 5)
    win_cols = any(sum_cols == 5)

    return win_rows or win_cols


# Get input
current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('5/input.txt', 'r')
elif current_directory[-1:] == "2":
    file = open('input.txt', 'r')

input = file.readlines()

environment =[[0]]

for vent in input:
    [start, end] = vent.strip("\n").split(" -> ")
    start = start.split(",")
    end = end.split(",")
    x_unsorted = [int(start[0]), int(end[0])]
    y_unsorted = [int(start[1]), int(end[1])]
    x = x_unsorted.copy()
    y = y_unsorted.copy()
    x.sort()
    y.sort()

    # Vertical
    # Extend array if necessary
    while len(environment) <= y[1]:
        environment.append([0 for _ in range(len(environment[0]))])

    # Horizontal
    # Extend array if necessary
    while len(environment[0]) <= x[1]:
        for row in environment:
            row.append(0)

    if x[0] == x[1]:
        # Add values
        for i in range(y[0], y[1]+1):
            environment[i][x[0]] += 1
    elif y[0] == y[1]:
        # Add values
        for i in range(x[0], x[1]+1):
            environment[y[1]][i] += 1
    else:
        # Add values
        j = y_unsorted[0]
        i = x_unsorted[0]
        for _ in range(x[0], x[1]+1):
            environment[j][i] += 1
            if j < y_unsorted[1]:
                j +=1
            else:
                j -= 1
            if i < x_unsorted[1]:
                i += 1
            else:
                i -= 1

        

environment = np.array(environment).astype(int)

plt.imshow(environment)
plt.show()

at_least_2 = environment >= 2

print(np.sum(at_least_2))
