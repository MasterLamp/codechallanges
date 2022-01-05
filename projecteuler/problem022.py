with open('projecteuler/problem022_names.txt', "r") as file:
    data = file.read()
    data = data.split(",")
    data.sort()
    sumName = 0
    nameIndex = 1
    for n in data:
        #clear quotes
        n = n.replace("\"","")
        #convert to ascii and remove offset(64)
        nameSum = sum((ord(n[l])-64) for l in range(len(n)))
        sumName += (nameSum*nameIndex)
        nameIndex += 1