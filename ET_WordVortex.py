"""I did need to look up a few things that you haven't taught yet, like mi, doing 2d arrays in python, etc.
It is done though!"""

def vortex(word):
    wordVortex = []
    Length = len(word) * 2 - 1  # Gets the length of the middle word
    for row in range(Length):
        wordVortex.append([])  # Creates the duble array
        for column in range(Length):
            wordVortex[row].append(word[min(row, column, Length - row - 1,
                                            Length - column - 1)])  # adds the letter to its respectable place.

    for i in range(len(wordVortex)):
        for j in range(len(wordVortex[i])):
            print wordVortex[i][j],
        print


def Main():
    vortex(raw_input("Enter a word or phrase."))


Main()

