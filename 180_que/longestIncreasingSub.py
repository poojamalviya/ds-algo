def lis(arr):
    return reclis(arr, -1, 0)

def reclis(num, prev, index):
    if index == len(num):
        return 0
    taken =0
    if num[index]>prev:
        taken = 1+ reclis(num, num[index], index+1)
    nottaken = reclis(num, prev, index+1)
    return max(taken, nottaken)

def dplis(arr):
    dp= [1]*len(arr)
    j =0
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i]>arr[j] and dp[i]<dp[j]+1:
                dp[i] =dp[j]+1
    return dp[-1]


arr = [10, 22, 9, 33, 21, 50, 41, 60]#[10,9,2,5,3,7,101,18]
#     [0,1, 2 3,4,5, 6, 7]
#   [1, 1, 1, 2, 2, 3, 4, 4]

print lis(arr)
print dplis(arr)


