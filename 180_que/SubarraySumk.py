def subArraySum(a, k):
    res = 0
    i =0
    s = {0:1}
    cm= 0
    for i in a:
        cm = cm +i
        if cm-k in s:
            res = res +s[cm-k]
        if cm in s:
            s[cm] = s[cm] +1
        else:
            s[cm] =1
    return res



# a = [23, 2, 4, 6, 7]  
a= [1,1,1]
k=2
print subArraySum(a, k)