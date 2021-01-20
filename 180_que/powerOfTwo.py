def isPowerOfTwo(n):
    _binary = getBinary(n)
    # print str(binary)
    binary = str(_binary)
    for i in len(binary)-1:
        if binary[-1] == 0:
            return False
        if i == 1:
            return False
    return True
def getBinary(n):
    res = ''
    while n>1:
        rem = n%2
        res = res + str(rem)
        n =n//2
    return res+str(1)


print isPowerOfTwo(8)
