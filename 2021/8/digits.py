import enum
import os
import numpy as np
import time

def part_1(file):
    count = 0

    for line in file:
        (i, o) = line.split(' | ')
        o = np.array(o.strip("\n").split(" "))

        for i in o:
            if len(i) in [2, 4, 3, 7]:
                count += 1

    print(count)

def part_2(file):
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    final_sum = 0

    for line in file:
        (i, o) = line.split(' | ')

        # decode input
        position = {}

        # Get number of each letter in total
        number_letters = []   
        for i_letter in range(len(letters)):
            number_letters.append(i.count(letters[i_letter]))

        i = np.array(i.split(" "))

        # use 4
        # determine position 1,2,3,5
        for input_number in i:
            if len(input_number) == 4:
                for letter in input_number:
                    if number_letters[letters.index(letter)] == 8:
                        position[2] = letter
                    elif number_letters[letters.index(letter)] == 9:
                        position[5] = letter
                    elif number_letters[letters.index(letter)] == 6:
                        position[1] = letter
                    elif number_letters[letters.index(letter)] == 7:
                        position[3] = letter

        # Fill in last positions 0,4,6
        for i_letter, letter in enumerate(letters):
            if letter not in position.values():
                if number_letters[letters.index(letter)] == 8:
                    position[0] = letter
                elif number_letters[letters.index(letter)] == 4:
                    position[4] = letter
                elif number_letters[letters.index(letter)] == 7:
                    position[6] = letter

        # determine output
        o = np.array(o.strip("\n").split(" "))

        numbers = []
        for number in o:
            if len(number) == 5:
                # digit 5,2 or 3
                if position[1] in number:
                    numbers.append(5)
                elif position[4] in number:
                    numbers.append(2)
                else:
                    numbers.append(3)
            elif len(number) == 6:
                # digit 9,6, or 0
                if not (position[3] in number):
                    numbers.append(0)
                elif position[2] in number:
                    numbers.append(9)
                else:
                    numbers.append(6)
            elif len(number) == 2:
                numbers.append(1)
            elif len(number) == 4:
                numbers.append(4)
            elif len(number) == 3:
                numbers.append(7)
            elif len(number) == 7:
                numbers.append(8)

        final_sum += numbers[0]*1000 + numbers[1]*100 + numbers[2]*10 + numbers[3]

    print(final_sum)

timenow = time.time()
dir = os.getcwd()

if dir[-19:] == "Advent_Of_Code_2021":
    file = open('8/input.txt', 'r')
elif dir[-1:] == "2":
    file = open('input.txt', 'r')

file= file.readlines()
#part_1(file)
part_2(file)

timeend = time.time()
print(f"Execution time: {timeend- timenow}")






