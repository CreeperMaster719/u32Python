num = 0
isTrue = False
while isTrue == False:
    num += 1
    for i in range(1,20):
        if num % 19 != 0 or num % 7 != 0 or num % 13 != 0 or num % 17 != 0 or num % 3 != 0 or num % 2 != 0:
            break
        if num % i != 0:
            break
        elif i >= 20 and num % i == 0:
            isTrue = True
            break
    print num
print num


