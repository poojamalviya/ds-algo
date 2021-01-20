def addBinary(a,b):
    carry = 0
    m = len(a)-1
    n = len(b)-1
    res= ""
    while m>=0 or n>=0:
        sumi = 0
        if carry: sumi = 1
        if m>=0: 
            sumi = sumi + int(a[m])
            m -=1
        if n>=0: 
            sumi = sumi + int(b[n])
            n -=1
        print sumi
        res = res + str(sumi %2)
        carry= sumi//2
    print res, carry, "ca"
    if carry: 
        res = res + str(carry)
    return res[::-1]

a = "11"
b = "1"
# 100
# a = "1010" 
# b = "1011"
# 10101

print(addBinary(a, b))