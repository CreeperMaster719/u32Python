# Code written by Eliot Troop
# Fibonacci Sequence Generator
#v1

def fibSequence(numberinput):
    a = 0
    b = 1
    newTotal = 0
    evenTotal = 0
    if(numberinput < 0):
        print "You have entered a number that cannot be applied here. Please try again."
    elif (numberinput == 0):
        return a
    elif (numberinput == 1):
        return b
    else:
        for i in range(2,numberinput):
            c = a + b
            a = b
            b = c
            if c >= 4000000:
                print "This program will not calculate any fibonacci numbers above 4 million."
                break
            newTotal = newTotal + c
            if c % 2 == 0:
                evenTotal += c
            print c


        total = c
    print "Your final number is " + str(total)
    print "All numbers added up are " + str(newTotal)
    print "All EVEN numbers added up are" + str(evenTotal)

print fibSequence(int(raw_input("Please enter the number you want the fibonacci sequence to go to.")))


