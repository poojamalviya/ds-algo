
def largestIncresingSub(a):
    res =1
    cur =1
    for i in range(0, len(a)-1):
        if a[i]< a[i+1]:
            cur += 1
        else:
            cur =1
        res = max(res, cur)
    return res
        

a= [1,3,5,4,2,3,4,5]
print(largestIncresingSub(a))