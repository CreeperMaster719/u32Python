primeList = []
sentinel = True
num = 2
while sentinel:

    if len(primeList) == 100:
        sentinel = False
        print primeList
    else:
        for x in range(num - 1, 1, -1):
            if num % x == 0:
                break
            else:
                primeList.append(num)
                print num
    num = num + 1
