def bfflipZero(arr):
    res = 0
    maxOne = 0
    for i in range(0, len(arr)-1):
        if arr[i] == 0:
            res += 1
        if arr[i] == 1:
            temp = 0
            for j in range(i, len(arr)-1):
                if arr[j] == 1:
                    temp += 1
            maxOne = max(maxOne, temp)

    return res + maxOne


    
def optimized(arr):
    cur = arr[0]
    res = arr[0]
    num =0
    for i in range(0, len(arr)-1):
        if arr[i] == 0:
            num += 1
        cur = max(arr[i], cur+arr[i])
        res = max(res, cur)
    return num+res

arr = [0, 1, 0, 0, 1, 1, 0]

print(bfflipZero(arr))
print(optimized(arr))