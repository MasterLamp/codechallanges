def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n // 10, partial * 10 + n % 10)

savedP = 0
for o in range(999):
    for i in range(999):
        trial = o * i
        if ReverseNumber(trial) == trial:
            if(savedP < trial):
                savedP = trial

print(savedP)