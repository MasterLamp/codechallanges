import pandas as pd
import sys
import time

accForUpVote = hiveautomation.GetAccountsForUpVote(sys.argv[1])
sonarreads = []
file = open('/home/masterlamps/adventofcode/2021/day1_input.txt', "r") 
for line in file: 
 sonarreads += [line.replace("\n","")]

increase = 0

lastValue = -1
i = 0
while i < len(sonarreads):
 if lastValue == -1:
     lastValue = sonarreads[i]
     increase += 1
     continue
 else:
     if sonarreads[i] > lastValue:
         print(str(sonarreads[i]) + " Increase")
         increase += 1
     else:
         print(str(sonarreads[i]) + " None-crease")
     lastValue = sonarreads[i]
 i += 1

i = 0
a = 0
b = 0 
c = 0
d = 0
e = 0
while i < len(sonarreads):
    a = 