def helper(data, k):
    if k == 0:
        return 1
    s = len(data) - k

    if data[s] == '0':
        return 0
    
    result = helper(data, k-1)

    if k >= 2 and int(data[s: s+2]) <= 26:
        result += helper(data, k-2)
    
    return result

def decodeWays(data):
    return helper(data, len(data))

def decodeway_dp(s):
    dp =[0]*10
    dp[1] = 0 if s[0] is 0 else 1

    for i in range(2, len(s)):
        one = int(s[i-1:i])
        two = int(s[i-2:i])

        print(one, two)

        if one >=1:
            dp[i] += dp[i-1]

        if two >=10 and two <=26:
            dp[i] += dp[i-2]
    
    print(dp)
    return dp[len(s)-1]


    


str1= "12345"

# print(decodeWays(str1))
print(decodeway_dp(str1))