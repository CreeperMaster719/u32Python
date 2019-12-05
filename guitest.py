# Gooey with easygui.py

import easygui


def main():
    " easygui.py tools "

    # messagebox
    response = easygui.msgbox("Raider Sandwich!")
    print "user clicked ", response

    # buttonbox
    favoriteSB = easygui.buttonbox("What is your favorite number?", choices=["47", "12", "88", "99", "infinity"])
    easygui.msgbox("You chose: " + favoriteSB + "!  Rock on dude!")

    # choicebox
    myBand = easygui.choicebox("What is your favorite band?", choices=["Led Zepplin", "Pink Floyd", "Phish", "Justin"])
    if myBand == "Cancel":
        easygui.msgbox("Be that way!")

    easygui.msgbox("You chose: " + myBand + "!  Rock on dude!")

    # enterbox
    myBalance = float(easygui.enterbox("What is your current balance? ", default="0.0"))
    easygui.msgbox("You like " + str(myBalance + 2) + " too?!  Rock on dude!")

    # integerbox
    age = easygui.integerbox("How old are you?")
    easygui.msgbox("Wow! You are " + str(age) + " years old!")  # note str()cast here to allow concatination!

    yee = easygui.enterbox("What is your favorite Fortnite dance", default="default dance")
    easygui.msgbox("*clap clap* you also like " + str(yee) + "! Nice moves dude!")
main()