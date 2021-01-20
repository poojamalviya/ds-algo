def maxSubArr(arr):
    maxtill = arr[0]
    sumtill = arr[0]

    if len(arr) == 1:
        return sumtill

    for i in range(1, len(arr)):
        maxtill = max(arr[i], maxtill+arr[i])
        # if maxtill > sumtill:
        #     sumtill =maxtill
        sumtill = max(sumtill, maxtill)
    return sumtill





# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [1, 2]
# arr = [-2,1]
print(maxSubArr(arr))
# ans = 6