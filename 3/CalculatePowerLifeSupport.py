import os
import numpy as np


def get_rating(input_data, most_common):
    # Delete according to criteria for oxygen generator rating
    modified_data = input_data
    for i in range(len(input_data[0])):
        # Get criteria in bit position i
        sum_value = sum(modified_data[:, i])
        half_len_data = len(modified_data)/2
        if most_common:
            criteria = int(sum_value >= half_len_data)
        else:
            criteria = int(sum_value < half_len_data)

        sorted_indexes = modified_data[:, i].argsort()
        modified_data = modified_data[sorted_indexes]
        check_array = modified_data[:, i]
        first_i_non_zero = np.nonzero(check_array)
        if len(first_i_non_zero[0]) == 0:
            continue
        first_i_non_zero = first_i_non_zero[0][0]

        if criteria == 1:
            modified_data = modified_data[first_i_non_zero:, :]
        elif criteria == 0:
            modified_data = modified_data[:first_i_non_zero, :]

        if len(modified_data) == 1:
            break

    return modified_data[0]

# Get input
current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('3/input.txt', 'r')
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

# Get most common rates of 1 or 0
O2_rate = get_rating(input_data, most_common=True).astype(int)

# Get least common rates of 1 or 0
CO2_rate = get_rating(input_data, most_common=False).astype(int)

# Convert to string
O2_rate = "".join([str(e) for e in O2_rate])
CO2_rate = "".join([str(e) for e in CO2_rate])
print(f"bin {O2_rate =}")
print(f"bin {CO2_rate =}")

# Convert to integer
O2_rate = int(O2_rate, 2)
CO2_rate = int(CO2_rate, 2)

# Print all
print(f"dec {O2_rate =}")
print(f"dec {CO2_rate =}")
print(f"Life support = {O2_rate*CO2_rate}")




