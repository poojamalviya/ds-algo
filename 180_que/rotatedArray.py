def findMin(arr):
    left, right = 0, len(arr)-1
    while left<right:
        mid = (right+left)//2
        if arr[mid]>arr[right]:
            left =mid+1
        else:
            right = mid
    return arr[left]

arr =[3,4,5,8, 9, 13, 20, 1,2]

# print findMin(arr)

def findTarget(arr, target):
    left, right = 0, len(arr)-1
    while(left<right):
        mid = (left+right)//2
        if arr[left] == target:
            return left
        elif arr[left]<target:



nums = [4,5,6,7,0,1,2] 
target = 0

print findTarget(nums, target)