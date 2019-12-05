import easygui


# Eliot's Grade Calculator a0.1.1
# Started Thur Oct 3, 2019 @ 9:00AM
# Finished Thur Oct 10, 2019 @ 12:55PM

def Main():  # The space for the main function of the program.
    easygui.msgbox("Welcome to Grade Letter Calculator. Get ready to enter your percentage from 0 to 100.")
    leave = False  # Sentinel variable for allowing user to exit the program.
    grade = ""  # The letter grade.
    ext = ""  # The + or -.
    perfect = False # a 100% or an F gives makes this true.
    while (not leave): # THis keeps the program running.
        gradePercent = float(easygui.enterbox("Please enter the grade.")) # Asks the user for the grade.
        '''THis next part determines what the grade is by checking if the value is less than a certain number, 
        and until that is true, it just keeps on looking until it hits 100, the highest possible number for this 
        program to accept. '''
        if (gradePercent < 60):
            grade = "F"
            perfect = True
        elif (gradePercent <= 69):
            grade = "D"
        elif (gradePercent <= 79):
            grade = "C"
        elif (gradePercent <= 89):
            grade = "B"
        elif (gradePercent <= 99):
            grade = "A"
        elif (gradePercent == 100):
            grade = "A"
            perfect = True
            ext = "+"
        else:
            print "Please enter a valid grade."
            break

        if (grade != "F" and not perfect): # This checks if the grade isn't an F and it isn't perfect. The "grade !=
            # "F"" is just redundancy.
            if (gradePercent % 10 >= 7.50):
                ext = "+"
            elif (gradePercent % 10 <= 2.49):
                ext = "-"
            else:
                ext = ""

        '''This code does nothing. It was a previous attempt that works, but it doesn't actually run during the 
        program's cycle. '''
        # elif (gradePercent < 70 and gradePercent >= 60):
        #     if(gradePercent < 62.5):
        #         easygui.msgbox("The grade is a D-")
        #     elif(gradePercent >= 62.5 and gradePercent < 67.5):
        #         easygui.msgbox("The grade is a D.")
        #     else:
        #         easygui.msgbox("The grade is a D+.")
        # elif (gradePercent < 80 and gradePercent >= 70):
        #     if(gradePercent < 72.5):
        #         easygui.msgbox("The grade is a C-")
        #     elif(gradePercent >= 72.5 and gradePercent < 77.5):
        #         easygui.msgbox("The grade is a C.")
        #     else:
        #         easygui.msgbox("The grade is a C+.")
        # elif (gradePercent < 90 and gradePercent >= 80):
        #     if(gradePercent < 82.5):
        #         easygui.msgbox("The grade is a B-")
        #     elif(gradePercent >= 82.5 and gradePercent < 87.5):
        #         easygui.msgbox("The grade is a B.")
        #     else:
        #         easygui.msgbox("The grade is a B+.")
        # elif (gradePercent < 100 and gradePercent >= 90):
        #     if(gradePercent < 92.5):
        #         easygui.msgbox("The grade is a A-")
        #     elif(gradePercent >= 92.5 and gradePercent < 97.5):
        #         easygui.msgbox("The grade is a A.")
        #     else:
        #         easygui.msgbox("The grade is a A+.")

        easygui.msgbox("The grade is " + grade + ext + ".") # Outputs the letter grade with extension.
        leaver = easygui.buttonbox("Do you want to leave? ", choices=["Yes", "No"]) #Asks the user if they wish to exit.
        if (leaver == "Yes"): #The check.
            leave = True
        else:
            leave = False


Main() #Allows all code in Main to run.
