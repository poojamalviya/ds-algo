
def partition(arr):
    total= sum(arr)
    if total & 1:
        return False
    target = total//2
    return dfs(arr, target, 0, {})

def dfs(arr, target, index, d):
    curr = str(index) + "-"+str(target) 
    if curr in d:
        return d.get(curr)
    if target == 0:
        return True
    if target<0 or index>len(arr)-1:
        return False
    res = dfs(arr, target-arr[index], index+1, d) or dfs(arr, target, index+1, d)
    d[curr] =res
    return res



arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]
# arr = [1, 5, 11, 5]

print partition(arr)