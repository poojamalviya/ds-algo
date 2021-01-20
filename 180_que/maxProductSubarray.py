def maxProductSubarray(arr):
    finalmax = arr[0]
    currentmax =arr[0]
    currentmin =arr[0]
    for i in range(1,len(arr)):
        temp = currentmax
        currentmax = max(currentmax*arr[i], arr[i], currentmin*arr[i])
        currentmin = min(arr[i], temp*arr[i], currentmin*arr[i])
        finalmax = max(finalmax, currentmax)
    return finalmax

        


arr = [-4,-3,-2] #[2,3,-2,4]
print maxProductSubarray(arr)

