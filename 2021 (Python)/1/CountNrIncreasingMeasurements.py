import os


current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('1/input.txt', 'r')
elif current_directory[-1:] == "1":
    file = open('input.txt', 'r')

input = file.readlines()

input = [int(i.strip("\n")) for i in input]

prev_data = input[0]
nr_increase = 0

for data in input:
    if prev_data < data:
        nr_increase += 1

    prev_data = data

print(nr_increase)
