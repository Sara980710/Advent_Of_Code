import os
import numpy as np

# Get input
current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('3/input_mamma.txt', 'r')
elif current_directory[-1:] == "2":
    file = open('input.txt', 'r')

input = file.read()

input = input.split('\n')

# Get length
binary_len = len(input[0])
nr_strings = len(input)

# Get sum input data per column
input_data = np.zeros([nr_strings, binary_len])

for i, bin_string in enumerate(input):
    bin_array = np.array([int(e) for e in bin_string])
    input_data[i, :] = bin_array

sum_data = sum(input_data)

# Get rates
gamma_rate = np.array(sum_data > nr_strings/2).astype(int)
epsilon_rate = np.abs(gamma_rate -1)

# Convert to string
gamma_rate = "".join([str(e) for e in gamma_rate])
epsilon_rate = "".join([str(e) for e in epsilon_rate])
print(f"bin gamma: {gamma_rate}")
print(f"bin epsilon: {epsilon_rate}")

# Convert to integer
gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)

# Print all
print(f"dec gamma: {gamma_rate}")
print(f"dec epsilon: {epsilon_rate}")
print(f"Power consumption = {gamma_rate*epsilon_rate}")




