def waterContainer(arr):
    if len(arr) == 0:
        return 0
    res = 0
    i, j = 0, len(arr)-1
    while(i<j):
        width = (j-i) +1
        mini = (arr[i], arr[j])
        res = max(mini*width, res)
        i = i+1
        j = j-1
    return res


arr = [2,1,5,6,2,3]
# print waterContainer(arr)
