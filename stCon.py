def getCount(s, n, b, c):
    if b < 0 or c < 0:
        return 0
    if n ==0:
        return 1
    if b == 0 and c == 0:
        return 1
    res = getCount(s, n-1, b, c)
    res += getCount(s, n-1, b-1, c)
    res += getCount(s, n-1, b, c-1)
    return res


n = 3
b_count = 1
c_count = 2

s = list('abc')

print (getCount(s, n, b_count, c_count))