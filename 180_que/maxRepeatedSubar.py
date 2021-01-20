def maxRepeatedSubarray(a,b):
    m = len(a)+1
    n = len(b)+1
    res =0
    dp = [[0]*(n) for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            if a[i-1] ==b[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                res = max(dp[i][j], res)
    return res

A= [1,2,3,2,1]
B= [3,2,1,6,7]
# o/p=3

print maxRepeatedSubarray(A, B)


