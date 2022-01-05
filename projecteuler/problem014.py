s = 0
savedS = 0
result = 0

for n in reversed(range(1000000)):
    s = 1
    curN = n
    for i in reversed(range(n)):
        #print(n)
        if((n % 2) == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        s += 1
        if(n == 1):
            #print(n)
            break
    if(savedS < s):
        result = s
        savedS = s
        print(str(curN) + " " + str(result))

print(result)