sum = 0
num = 0
count = 0
while(count <= 999):
    num = num + 1
    if(num % 3 == 0 or num % 5 == 0 or num % 2 == 0 or num % 7 == 0 or num % 11 == 0):
        sum = sum + num
    else:
        print num
    count = count + 1
print sum
