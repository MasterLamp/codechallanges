#shortcut to result
number = 232790000
ok = True

while True:
    if((number % 1) == 0) and \
    ((number % 2) == 0) and \
    ((number % 3) == 0) and \
    ((number % 4) == 0) and \
    ((number % 5) == 0) and \
    ((number % 6) == 0) and \
    ((number % 7) == 0) and \
    ((number % 8) == 0) and \
    ((number % 9) == 0) and \
    ((number % 10) == 0) and \
    ((number % 11) == 0) and \
    ((number % 12) == 0) and \
    ((number % 13) == 0) and \
    ((number % 14) == 0) and \
    ((number % 15) == 0) and \
    ((number % 16) == 0) and \
    ((number % 17) == 0) and \
    ((number % 18) == 0) and \
    ((number % 19) == 0) and \
    ((number % 20) == 0):
        ok = True
    else:
        ok = False
    print("current number " + str(number))
    if(ok == False):
        number += 1
    else:
        break

print(number)