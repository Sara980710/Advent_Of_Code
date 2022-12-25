import os


current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('1/input.txt', 'r')
elif current_directory[-1:] == "1":
    file = open('input.txt', 'r')
    
input = file.readlines()

input = [int(i.strip("\n")) for i in input]

nr_increase = 0
prev_sum_3 = sum(input[0:3])

for i_data in range(1,len(input)):
    sum_3 = sum(input[i_data:i_data+3])
    if prev_sum_3 < sum_3:
        nr_increase += 1

    prev_sum_3 = sum_3


print(nr_increase)
