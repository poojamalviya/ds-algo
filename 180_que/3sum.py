def fixPosition(arr):
    res = []
    temp =[]
    arr.sort()
    dfs(arr, 0, res, temp, 0)
    return res


def dfs(arr, index, res, temp, su):
    print index, temp
    import time
    time.sleep(1)
    if len(temp) == 3 and su ==0:
        # print temp
        res.append(temp)
    for i in range(index, len(arr)):
        dfs(arr, i+1, res, temp+[arr[i]], su-arr[i])

def threeSum(arr):
    res = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] ==0:
                    res.append([arr[i], arr[j], arr[k]])
    return res

nums = [-1, 0, 1, 2, -1, -4]
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# print threeSum(nums)
print threeSum(nums)
print fixPosition(nums)