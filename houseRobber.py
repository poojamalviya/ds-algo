def maxMoney(arr, n, i):
    print i
    if i==n:
        return
    if i==n-1:
        return arr[i]
    if i == n-2:
        return max(arr[n-1], arr[n-2])
    return max(arr[i]+ maxMoney(arr, n, i+2), maxMoney(arr, n, i+1)) 
    

def houseRobber(h):
    res = [0] * int(len(h))
    res[0] = h[0]
    res[1] = max(h[0], h[1])
    print res, "- - - "
    for i in range(2, len(h)):
        res[i] = max(h[i]+res[i-2], res[i-1])
    print res
    return res[len(res)-1]


h= [2,7,9,3,1]
# print maxMoney(h, len(h), 0)
print houseRobber(h)
