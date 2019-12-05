'''
Super cool temperature converter
Made by Eliot Troop
easygui and playsound used
:)
'''

import easygui
import playsound
choice = ""
def tempConvertC(tempF):
    tempC = ((5.0 / 9) * ((tempF) - 32))
    easygui.msgbox("Your temperature in Celsius is " + str(tempC), "Celsius temperature")
    playsound.playsound("button-30.mp3")


# COnverts to Fahrenheit
def tempConvertF(tempC):
    tempF = (((9.0 / 5) * tempC) + 32)
    easygui.msgbox("Your temperature in Fahrenheit is " + str(tempF), "Fahrenheit temperature")
    playsound.playsound("button-25.mp3")


while choice != "Exit":
    choice = easygui.buttonbox("Do you want to convert from C to F or F to C? If not, press the Exit button.", choices=["C-F", "F-C", "Exit"])
    playsound.playsound("button-29.mp3")
    if(choice == "C-F"):
       celcel =  float(easygui.enterbox("Please enter your value in Celsius"))
       tempConvertF(celcel)
    elif(choice == "F-C"):
        farfar = float(easygui.enterbox("Please enter your value in Fahrenheit."))
        tempConvertC(farfar)

'''usernameandpassword = easygui.enterbox("First, could you please enter your username and password to your life separated by a comma?")
easygui.msgbox("MUAHAHAHAAHAHAH! Your username and password are " + usernameandpassword)'''

playsound.playsound("beep-09.mp3")

