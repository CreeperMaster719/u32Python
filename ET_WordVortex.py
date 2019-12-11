def vortex(word):
    wordVortex = []
    Length = len(word) * 2 - 1
    for row in range(Length):
        wordVortex.append([])
        for column in range(Length):
            wordVortex[row].append(word[min(row, column, Length - row - 1, Length - column - 1)])

    for i in range(len(wordVortex)):
        for j in range(len(wordVortex[i])):
            print wordVortex[i][j],
        print


def Main():
    vortex(raw_input("Enter a word or phrase."))


Main()
