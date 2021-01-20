INT_MIN = -32767
  
# Returns the best obtainable price for a rod of length n and 
# price[] as prices of different pieces 
def cutRod(price, n): 
    val = [0 for x in range(n+1)] 
    val[0] = 0
  
    # Build the table val[] in bottom up manner and return 
    # the last entry from the table 
    for i in range(1, n+1): 
        max_val = INT_MIN 
        for j in range(i): 
            print i, j, price[j], val[i-j-1]
            max_val = max(max_val, price[j] + val[i-j-1]) 
        val[i] = max_val 

  
    return val[n] 
  
# Driver program to test above functions 
# arr = [1, 5, 8, 9, 10, 17, 17, 20] 
# size = len(arr) 
# print("Maximum Obtainable Value is " + str(cutRod(arr, size)))

def cuttingRod(prize, size):
    dp = [0]*(size+1)
    res = 0
    for i in range(1, size+1):
        for j in range(i):
            res = max(res, prize[j]+ dp[i-j-1])
            dp[i]= res
    return dp[-1]
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
print("Maximum Obtainable Value is " + str(cuttingRod(arr, size)))