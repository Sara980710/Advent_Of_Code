import os


current_directory = os.getcwd()

if current_directory[-19:] == "Advent_Of_Code_2021":
    file = open('2/input.txt', 'r')
elif current_directory[-1:] == "2":
    file = open('input.txt', 'r')

input = file.read()

input = input.split('\n')

logitude = 0 # vertical
latitude = 0 # horizontal

for data in input:
    [direction, magnitude] = data.split(" ")
    magnitude = int(magnitude)

    if direction == "forward":
        latitude += magnitude
    elif direction == "down":
        logitude += magnitude
    elif direction == "up":
        logitude -= magnitude
    else:
        raise Exception("invalid input")

    
print(latitude*logitude)
