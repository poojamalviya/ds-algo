def editDistance(str1, str2, m, n):
    if m ==0:
        return n
    if n == 0:
        return m
    if str1[m-1] == str2[n-1]:
        return editDistance(str1, str2, m-1, n-1)
    return 1 + min(editDistance(str1, str2, m, n-1), #add
        editDistance(str1, str2, m-1, n), # delete
        editDistance(str1, str2, m-1, n-1)) #replace


def dp(str1, str2, m, n):
    if m==0 and n==0:
        return 0
    if m==0 and n>0:
        return n
    if m>0 and n==0:
        return m
    dp = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif str1[i-1] == str2[j-1]:
                dp[i][j]= dp[i-1][j-1]
            else:
                dp[i][j]= 1+ min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    print dp
    return dp[-1][-1]


str1 = "sunday"
str2 = "saturday"
print (editDistance(str1, str2, len(str1), len(str2)))
print (dp(str1, str2, len(str1), len(str2)))

