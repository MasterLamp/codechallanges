import sys
import time

moveReads = []
file = open('adventofcode/2021/day2_input.txt', "r") 
for line in file: 
 moveReads += [line.replace("\n","")]

horizontal = 0
vertical = 0
aim = 0

for move in moveReads:
    if("forward" in move):
        change = int(move[8:])
        horizontal += change
        vertical += aim * change
    elif("down" in move):
        change = int(move[5:])
        #vertical += int(move[5:])
        aim += change
    elif("up" in move):
        change = int(move[3:])
        #vertical -= change
        aim -= change

print(horizontal*vertical)
