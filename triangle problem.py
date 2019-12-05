combinations = 0
loops = 0
failNull = -1000
usedi = False
usedj = False
usedk = False
usedl = False
combos = list()
for i in range(1,13):
    for j in range(1,13):
        for k in range(1,13):
            for l in range(1,13):
                if(i==j or i==k or i ==l or j == k or j ==l or k == l):
                    failNull += 1
                else:
                    combos.append(i)
                    combos.append(j)
                    combos.append(k)
                    combos.append(l)
                    loops = loops + 4
                    if(combos[loops + 1] != i):

                        if(i+j+k+l == 26):
                            print str(i) + " " + str(j) + " " + str(k) + " " + str(l)
                            combinations = combinations + 1


print combinations
