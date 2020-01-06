count = 0
currentNum = 0
listy = []
while (len(listy) < 100):
    if (currentNum % 2 != 0 and currentNum % 3 != 0 and currentNum % 5 != 0 and currentNum % 7 != 0 and currentNum % 11 != 0 ):
        print currentNum

        listy.append(currentNum)

    currentNum += 1
print listy
