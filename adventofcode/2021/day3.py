import sys
import time

diagnosticReads = []
file = open('/home/masterlamps/adventofcode/2021/day3_input.txt', "r") 
for line in file: 
 diagnosticReads += [line.replace("\n","")]

resultOne = [0,0,0,0,0,0,0,0,0,0,0,0]
resultZero = [0,0,0,0,0,0,0,0,0,0,0,0]

for d in diagnosticReads:
    curPosition = 0
    while curPosition < len(d):
        if(d[curPosition] == "0"):
            resultZero[curPosition] += 1
        elif(d[curPosition] == "1"):
            resultOne[curPosition] +=1
        curPosition += 1

gammarate =   "111100111111"
gammaValue = int(gammarate, 2)
# int(binary, 2)
epsilonrate = "000011000000"
epsilonValue = int(epsilonrate, 2)