def combinationSum(arr, target):
    res = []
    dfs(arr, target, 0,res, [])
    return res
def dfs(arr, target, index, res, temp):
    if target<0:
        return
    if target ==0:
        res.append(temp)
        return 
    for i in range(index, len(arr)):
        dfs(arr, target-arr[i], i, res, temp+[arr[i]])

c= [2,3,6,7]
t = 7

# [
#   [7],
#   [2,2,3]
# ]

# c= [2,3,5]
# t = 8

# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

print combinationSum(c, t)