def mypow(i, n):
    res = 1
    counter = 0
    while counter<n:
        res = res * i
        counter = counter+1
    if n<0:
        res = 1//res
    return res


# Input = 2.00000
# n= 10
Input = 2.00000
n= -2
# Output: 1024.00000

print mypow(Input, n)
