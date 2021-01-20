
def rec(n):
    res ='1'
    for _ in range(0, n-1):
        print res
        res = strCount(res)
    return res




def strCount(s):
    count= 1
    res= ''
    for i in range(0, len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            count += 1
        else:
            res =  res + str(count) + str(s[i])
            count = 1
    return res


print(rec(6))
# "312211"
# 111221

