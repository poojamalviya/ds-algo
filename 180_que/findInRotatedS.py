def findInRotatedSortedArray(arr, tar):
    low, high = 0, len(arr)-1
    while low<=high:
        mid = (low+high)/2
        if arr[mid] == tar:
            return mid
        if arr[low]<arr[mid]:
            if arr[low]<=tar<=arr[mid]:
                high =mid-1
            else:
                low = mid+1
        else:
            if arr[mid]<=tar<=arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1
                




# arr = [4,5,6,7,1,2,3]
arr = [3,1]
print findInRotatedSortedArray(arr, 1)