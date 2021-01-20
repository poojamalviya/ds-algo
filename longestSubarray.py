def maxSum(arr):
    currentMax= 0
    maxSoFar= 0
    for i in range(0, len(arr)-1):
        currentMax = max(arr[i]+ arr[i+1], currentMax)

        if currentMax > maxSoFar:
            maxSoFar = currentMax
    
    return maxSoFar

arr = [-2, -3, 4, -1, -2, 1, 5, -3]; 

print maxSum(arr)

