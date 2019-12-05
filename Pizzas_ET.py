"""This program prints all possible permutations of prices for five pizza toppings. It is not the most efficient,
but I gave up and brute forced. Each for loop serves as a way to count one or zero for each topping. It displays the
total price to the right and the pizza size to the left. """
def pizzaTable():
    pizzaToppings = ["Pepperoni", "Cheese", "Basil", "Sausage", "NASTY pineapple"] #NAAASTY PINEAPPLE.
    pizzaPricesT = [1.00, 0.75, 1.50, 1.85, 10.00] #storing prices seperately.
    pizzaPrices = [10.95, 15.95, 20.95] #Same here.
    pizzaTypes = ["Small", "Medium", "Large"]
    print "Size            Pepperoni \tCheese \t \tBasil \t \tSausage\t \tNASTY pineapple \tPrice"
    for x in range(3):
        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        for e in range(2):
                            totalPrice = 0
                            totalPrice += pizzaPrices[x]
                            if a == 1:  totalPrice += pizzaPricesT[0]
                            if b == 1:  totalPrice += pizzaPricesT[1]
                            if c == 1:  totalPrice += pizzaPricesT[2]
                            if d == 1:  totalPrice += pizzaPricesT[3]
                            if e == 1:  totalPrice += pizzaPricesT[4]
                            print pizzaTypes[x] + "\t \t \t" + str(a) + "\t\t  \t" + str(b) + "\t \t \t" + str(c) + "\t " \
                                                  "\t \t" + str(d) + "\t \t \t" + str(e) + "\t \t \t \t \t", str(totalPrice) #Stpid stacks.



        print " "

def Main():
    pizzaTable()
Main()

