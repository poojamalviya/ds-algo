# (Subsets, Permutations, Combination Sum, Palindrome Partitioning)

def subset(a):
    res = []
    temp = []
    backtrack(res,temp, a, 0)
    return res

def backtrack(res,temp, a, start):
    # if level == len(a):
    res.append(temp)
    for i in range(start, len(a)):
        # temp+[a[i]]
        temp = temp.append(a[i])
        backtrack(res,temp, a, i+1)
        # temp.pop(len(temp)-1)

def subsets1(nums):
    res = []
    dfs(sorted(nums), 0, [], res)
    return res
    
def dfs(nums, index, path, res):
    print path
    res.append(path)
    for i in range(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], res)

def permute(nums):
    visited = set()
    res = []
    backtracking(res,visited,[],nums)
    return res
def backtracking(res,visited,subset,nums):
    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res,visited,subset+[nums[i]],nums)
            visited.remove(i)


a = [1,2,3]
print subsets1(a)
# print subsets(a)
print permute(a)