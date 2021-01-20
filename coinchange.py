def coinChange(arr, l, s):
    if s< 0:
        return 0
    if s==0:
        return 1
    if l <= 0 and s>=0:
        return 0
    return coinChange(arr, l, s-arr[l-1]) +  coinChange(arr, l-1, s)


def coinChange_dp(arr, sum):
    dp = [0] * sum
    dp[0] = 0
    for i in range(0, sum):
        for j in range(0, len(arr)):
            dp[i] = min(dp[i], 1+ dp[i-arr[j]])
            print(dp[i], arr[j], dp[i-arr[j]])
    return dp

arr =[1,2,3]
n = len(arr)
s= 5
print(coinChange(arr, n-1, s))
print (coinChange_dp(arr, s))