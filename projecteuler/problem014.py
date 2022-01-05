savedS = 0
savedN = 0

for n in reversed(range(1000000)):
    s = 0
    curN = n
    for i in reversed(range(n)):
        if((n % 2) == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        s += 1
        if(n == 1):
            break
    if(savedS < s):
        savedS = s
        savedN = curN

print(str(savedN) + " " + str(savedS))