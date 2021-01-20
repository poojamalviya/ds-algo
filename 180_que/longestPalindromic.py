

def longestPalindromicSubsequence(s):
    n=len(s)
    dp = [n*[0] for i in range(n)]
    for i in range(n):
        dp[i][i]= 1
    for length in range(1,n):
        for i in range(n-length):
            j = i+length
            if s[i]==s[j]:
                dp[i][j] = 2+ dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n-1]

def lpsRecursive(s, i, j):
    if s[i] ==s[j] and i+1==j:
        return 2
    if i==j:
        return 1
    if s[i]== s[j]:
        return 2+ lpsRecursive(s, i+1, j-1)
    else:
        return max(lpsRecursive(s, i+1,j), lpsRecursive(s, i, j-1)) 



a= "babad"
# b= "bbbab"
print longestPalindromicSubstring(a)
# print longestPalindromicSubsequence(b)
# print lpsRecursive(b, 0, len(b)-1)

