def isPalindrome(num):
    return str(num) == str(num)[::-1]
def largest(bottom, top):
    z = 0
    for x in range(top, bottom, -1):
        for y in range(top,bottom, -1):
            if isPalindrome(x*y):
                if x*y > z:
                    z = x*y
    return z
print largest(100,1000)

