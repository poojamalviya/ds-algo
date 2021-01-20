def summaryRange(arr):
    res = []
    s = None
    e = None
    for i in range(0, len(arr)):
        if arr[i] +1 == arr[i+1] and s== None:
            s= arr[i]
        if arr[i] +1 != arr[i+1]:
            e = arr[i]
            if s is None:
                res.append(arr[i])
            else:
                s = None
                res.append(str(str(s)+ "->" + str(e))
    return res



arr = [0,1,2,4,5,7]
# ["0->2","4->5","7"]

print summaryRange(arr)