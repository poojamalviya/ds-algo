def maxSumIncreasingSubsequence(arr):
    return helper(arr, -1, 0)
def helper(arr, prev, index):
    if index== len(arr):
        return 0
    taken = 0
    if arr[index]>prev:
        taken = taken+helper(arr, arr[index], index+1)
    notTaken = helper(arr, prev, index+1)
    return max(taken, notTaken)
arr = [1, 101, 2, 3, 100, 4, 5] 
print maxSumIncreasingSubsequence(arr)