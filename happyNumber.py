import time

def happyNumber(n):
    s =str(n)
    check = 0
    for i in s:
        if i is not 0:
            check += int(i)*int(i)
    print(i)
    time.sleep(5)
    if check != 1:
        return happyNumber(check)
    else:
        return True
              

# number = 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

print (happyNumber(2))