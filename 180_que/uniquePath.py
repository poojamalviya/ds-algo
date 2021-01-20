def uniquePath(m,n):
    dp = [[1]*n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]
    print dp
    return dp[-1][-1]


m = 3
n = 2
# 3

print uniquePath(m,n)
print uniquePaths(m,n)

# [[0, 0],
# [0, 0]
# [0, 0]]