import sys
import time

class boardEntry:
    value = 0
    marked = False

drawReads = [67,31,58,8,79,18,19,45,38,13,40,62,85,10,21,96,56,55,4,36,76,42,32,34,39,89,6,12,24,57,93,47,41,52,83,61,5,37,28,15,86,23,69,92,70,27,25,53,44,80,65,22,99,43,66,26,11,72,2,98,14,82,87,20,73,46,35,7,1,84,95,74,81,63,78,94,16,60,29,97,91,30,17,54,68,90,71,88,77,9,64,50,0,49,48,75,3,59,51,33]

boardReads = []
boardClassReads = []

file = open('adventofcode/2021/day4_input_boards.txt', "r") 
readLineNo = 1
curLine = 0
for line in file:
    if((readLineNo % 6) == 0):
        print("Next Board!")
        readLineNo = 1
        continue
    print("ReadLineNo:" + str(readLineNo))
    curArray = []
    curLine = line.replace("\n","")
    curLine = curLine.replace("  ", " ").strip()
    curBoardLine = []
    for l in curLine.split(" "):
        curBoardEntry = boardEntry()
        curBoardEntry.value = l
        curArray.append(l)
        curBoardLine.append(curBoardEntry)
    boardReads.append(curArray)
    boardClassReads.append(curBoardLine)
    readLineNo += 1

for draw in drawReads:
    boardIndex = 0 #0-4
    while True:
        lineIndex = 0
        while lineIndex < 5:
            pos = boardClassReads[boardIndex][lineIndex]
            if(int(pos.value) == draw):
                pos.marked = True
            lineIndex += 1
        boardIndex += 1
        if((boardIndex % 5) == 0):
            break