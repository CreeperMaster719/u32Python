user_score = 0
simon_pattern = str(31415926535897932384626433832795028841971693993751)
user_pattern  = raw_input()

''' Your solution goes here '''

for i in range(len(simon_pattern)):
    if(user_pattern[i] == simon_pattern[i]):
        user_score += 1
    else:
        break


print 'User score:', user_score