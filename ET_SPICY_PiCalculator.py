import math
import time
#Eliot Troop PI Generator
#Finished Tue, September 10, 2019
pi = 0.0
count = 0
denom = 1
flippityFlop = 1
while(pi != 3.14159265 or count == 1000):


    count = count + 1

    if(flippityFlop >= 0):
        flippityFlop = flippityFlop * -1
        pi += (4.0 / denom)
    else:
        flippityFlop = flippityFlop * -1
        pi -= (4.0 / denom)

    print pi
    denom = denom + 2
    pi = round(pi, 8)

print pi
print "It has been " + str(count) + " cycles."