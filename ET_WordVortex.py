word = raw_input("Enter a word")
vortex = len(word + word[-2:-len(word)-1:-1])
wordv=word + word[-2:-len(word)-1:-1]
wordlist = []
for i in wordv:
    wordlist.append(i)
for i in range(vortex):
    for j in range(vortex):
        print wordlist[i],
    print
