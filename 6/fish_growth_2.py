import os
import numpy as np
import time

timenow = time.time()
dir = os.getcwd()

if dir[-19:] == "Advent_Of_Code_2021":
    file = open('6/input.txt', 'r')
elif dir[-1:] == "2":
    file = open('input.txt', 'r')

input = np.array([int(i) for i in file.read().strip().split(',')])
(unique, count) = np.unique(input, return_counts = True)
frequencies = np.asarray((unique, count)).T[:, 1]
frequencies = np.append(np.zeros(1),frequencies)
frequencies = np.append(frequencies, np.zeros(10-len(frequencies)))


for day in range(256):
    zeros = frequencies[0]
    frequencies[0:-1] = frequencies[1:]
    
    # reset old fish
    frequencies[6] += zeros

    # new fish
    frequencies[8] += zeros

print(f'Number of fishes: {int(np.sum(frequencies))}')

timeend = time.time()

print(f"Execution time: {timeend- timenow}")
