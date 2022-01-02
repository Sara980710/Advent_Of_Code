import os
import numpy as np

dir = os.getcwd()

if dir[-19:] == "Advent_Of_Code_2021":
    file = open('6/input.txt', 'r')
elif dir[-1:] == "2":
    file = open('input.txt', 'r')

input = np.array([int(i) for i in file.read().strip().split(',')])

for day in range(80-1):
    input -= 1
    zeros = input == 0

    # reset old fish
    input = input + zeros*7

    # new fish
    summation = np.sum(zeros)
    
    input = np.append(input, np.ones(summation)*9)

print(len(input))