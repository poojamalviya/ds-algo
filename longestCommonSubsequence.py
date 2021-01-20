
def longestCommonSubsequence(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1]:
       return 1 + longestCommonSubsequence(x, y, m-1, n-1)

    return max(longestCommonSubsequence(x, y, m, n-1), longestCommonSubsequence(x, y, m-1, n))


def lcsDp(m, n):
    dp = [[0]* (len(m)+1) for x in range((len(n)+1))]
    print dp

    for i in range(1, len(m)+1):
        for j in range(1, len(n)+1):
            print i, j
            if m[i-1] == n[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i-1][j-1] = max(dp[i-1][j], dp[i][j-1])
    print dp

X = "ABCDE"
Y = "ACE"
# print ("Length of LCS is ", longestCommonSubsequence(X , Y, len(X), len(Y)))
lcsDp(list(X), list(Y))
