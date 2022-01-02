import os
import numpy as np
import time
import scipy.special


def check(best_horizontal, input):
    fuel_values = np.abs(input-best_horizontal)

    fuel = 0
    for f in fuel_values:
        fuel += np.sum(np.arange(f)+1)

    return fuel

def part_1(input):
    best_horizontal = np.median(input)

    fuel = np.sum(np.abs(input-best_horizontal))

    print(f"Best position: {best_horizontal}, fuel: {fuel}")


def part_2(input):
    meanof = np.mean(input)
    best_horizontal_1 = np.floor(meanof)
    best_horizontal_2 = np.ceil(meanof)
    fuel_1 = check(best_horizontal_1, input)
    fuel_2 = check(best_horizontal_2, input)

    if fuel_2 > fuel_1:
        print(f"Best position: {best_horizontal_1}, fuel: {fuel_1}")
    else:
        print(f"Best position: {best_horizontal_2}, fuel: {fuel_2}")

timenow = time.time()
dir = os.getcwd()

if dir[-19:] == "Advent_Of_Code_2021":
    file = open('7/input.txt', 'r')
elif dir[-1:] == "2":
    file = open('input.txt', 'r')

input = np.array([int(i) for i in file.read().strip().split(',')])

#part_1(input)
part_2(input)

timeend = time.time()
print(f"Execution time: {timeend- timenow}")
