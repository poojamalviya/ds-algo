def pathToTarget(arr):
    q = [[0]]
    res= []
    n = len(arr)-1
    while q:
        curr = q.pop()
        for i in arr[curr[-1]]:
            if i == n:
                res.append(curr+[i])
            else:
                curr.append(curr+[i])
    return res

def dfsSolution(arr):
    res= []
    def dfs(curr, path):
        if curr == len(arr)-1:
            res.append(path)
        for i in arr[curr]:
            dfs(i, path+[i])
    dfs(0,[0])
    return res



arr= [[1,2], [3], [3], []] 
# Output= [[0,1,3],[0,2,3]] 

# print pathToTarget(arr)
print dfsSolution(arr)