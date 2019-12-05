# Temperature converter.
# Eliot Troop
# C=(5/9)*(F-32)

# Converts to Celsius
def tempConvertC(tempF):
    tempC = ((5.0 / 9) * ((tempF) - 32))
    print tempC


# COnverts to Fahrenheit
def tempConvertF(tempC):
    tempF = (((9.0 / 5) * tempC) + 32)
    print tempF


# Choose and enter statement.
print "Welcome to the Temperature Converter. Type C for Celsius to Fahrenheit or F for Fahrenheit to Celsius.."
choice = raw_input("Enter C or F.")
if (choice == 'c'):
    userImput2 = int(raw_input("Please enter your temperature in Celsius."))
    tempConvertF(float(userImput2))
elif (choice == "f"):
    userInput = int(raw_input("Please enter your temperature in Fahrenheit."))
    tempConvertC(userInput)
# Completed 9/9/19 @ 8:40AM
