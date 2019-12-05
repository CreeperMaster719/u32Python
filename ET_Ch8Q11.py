# CODE BY ELIOT TROOP
import sys


def Main():
    stri = raw_input("Enter a name")
    for i in range(len(stri)):
        for x in range(len(stri)):
            print stri[x] * (i+1),  # My only mistake was where I put that comma. I wrote it before the * sign when it
            # had to be ae the end. It also had to be i+1 instead of i.
            sys.stdout.softspace = 0
        print


Main()
