def powerSet(arr):
    res =[]
    arr.sort()
    dfs(arr, res, [], 0)
    return res

def dfs(arr, res, temp, index):
    res.append(temp)
    for i in range(index, len(arr)):
        # if index<i and arr[i]==arr[i-1]:
        #     continue
        dfs(arr, res, temp+[arr[i]], i+1)
        


arr= [1,2,3]#[4,4,4,1,4]#[1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
print powerSet(arr)