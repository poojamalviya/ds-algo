def longestCommonSubsequence(arr):
    res =[]
    dfs(arr, 0, [], res)
    return res

def dfs(arr, index, temp, res):
    if len(temp)> len(res):
        res = temp
        

arr =[10,9,2,5,3,7,101,18]
print longestCommonSubsequence(arr)