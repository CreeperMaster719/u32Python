word = raw_input("Enter a word")
for i in range(len(word + word[-2:-len(word)-1:-1])):
    for j in range((len(word + word[-2:-len(word)-1:-1]))):
        print word[i],
    print
