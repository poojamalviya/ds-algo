def addDigit(num):
    res = 0
    while len(str(num)) !=0:
        for i in str(num):
            print i
            res = res + int(i)
        num= res
        print res, "res"

    return num



num= 38
# Output: 2 
print addDigit(num)