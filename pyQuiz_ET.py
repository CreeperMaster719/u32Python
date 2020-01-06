# Questions
"""Code by Eliot Troop"""

"""Question 1
birthdays = ['5-25', '7-19', '3-23', '7-10']
for i in range(len(birthdays)):
    print birthdays[i]
birthdays.append('9-22')
print birthdays
"""

"""Question 2
gameScores = [20, 25, 10, 40, 5]
sum = sum(gameScores)
avg = (sum * 1.0) / len(gameScores)
print (sum / avg) * min(gameScores)
"""

"""Question 3
userInput = [2, 8, 3, 'pepperoni', 5, 7, 9, 'cheese']
deleted = 0
for i in range(len(userInput)):
    if type(userInput[i - deleted]) == str:
        del userInput[i - deleted]
        deleted += 1
print userInput
"""

"""Question 4
findIt = ['blue', 'green', 'yellow', 'bob', 'orange']
removed = 0
for i in findIt:
    if not i == 'bob':
        findIt.remove(i)
print findIt
"""

"""Q5
ages = [2, 3, 5, 4, 'T', 9]
total = sum(ages)
for i in range(len(ages)):
    if total % ages == 1:
        print "Baby"
"""

"""Q6
nums = [1, 8, 2, 3, 6, 5, 9, 4, 7, 12, 10, 13, 11]
for i in range(len(nums)):
    if not nums[i] % 2 == 0:
        del nums[i]
print nums
"""
"""Q7
word = "rainbow quartz 2.0"
for i in range(word):
    if word[i].isdigit():
        print word[i]
"""

"""Q8
num = 1800.25
str = str(num) + 2
for i in str:
    print str * 2
"""

"""Q9
nums = [2, 3, 2, 5, 9, 8, 4, 1, 100, 3, 1]
removed = 0
for i in range(len(nums)):
    if nums[i-removed] > 5:
       del nums[i-removed]
       removed += 1
for i in range(len(nums)):
    print nums[i],
"""
"""Q10
cakes = ["rainbow", "marbled", "vanilla", "chocolate", "volcano", "gummy"]
price = 0
for i in cakes:
    if ord(i[0]) > ord('a') and ord(i[0]) < ord('o'):
        price += ord(i[0])
        print i,
        print price
"""

"""Q11
for i in [1,8]:
    for j in [1, 8]:
        for k in [1,8]:
            print i+j+k,
"""

"""Q12

"""
sentinel = True
numb = 0.0
sum = 0.0
nums = []
while sentinel:
    if numb % 2 == 0:
        nums.append(numb)
        if numb % 3 == 0:
            nums.append(numb)
            if numb > 100:
                nums.append(numb)
                if numb % 5 == 0:
                    nums.append(numb)
                    print numb
                    sentinel = False
    numb += 1
    for i in range(len(nums)):
        sum += nums[i]
print sum
