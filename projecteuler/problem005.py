#shortcut to result
number = 232790000
ok = False

while True:
    if((number % 1) == 0):
        ok = True
    else:
        ok = False
    if((number % 2) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 3) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 4) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 5) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 6) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 7) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 8) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 9) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 10) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 11) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 12) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 13) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 14) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 15) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 16) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 17) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 18) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 19) == 0):
        ok = True and ok
    else:
        ok = False
    if((number % 20) == 0):
        ok = True and ok
    else:
        ok = False
    print("current number " + str(number))
    if(ok == False):
        number += 1
    else:
        break

print(number)