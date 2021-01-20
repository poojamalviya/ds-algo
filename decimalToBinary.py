def decimalBinary(n):
    binary = '{:032b}'.format(n)
    res =''
    for i in range(len(binary)-1,-1, -1):
        res += binary[i]
    return int(res, 2)

def reverse(x):
    res =''
    s = str(x)
    if s[0] == '-':
        res = '-'
        for i in range(len(s)-1, 0, -1):
            res += s[i]
    else:
        for i in range(len(s)-1, -1, -1):
            res += s[i]
    return int(res)


def compliment(num):
    binary = format(num, 'b')
    res = ''
    for i in list(binary):
        if i== '0':
            res =  res+"1"
        else:
            res = res+ "0"
    return int(res, 2)

# print decimalBinary(43261596)
# print(reverse(-123))
print compliment(5)
