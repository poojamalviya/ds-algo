def maxSlidingWindow(arr, k):
    res = []
    for i in range(len(arr)+1-k):
        j = i +k
        temp =[]
        for dig in range(i, j):
            temp.append(arr[dig])
        res.append(max(temp))
    return res

def optimized(arr, k):
    res =[]
    temp = [0]*k
    for i in range(len(arr)):
        if i <=k-1:
            temp.append(arr[i])
            if i==k-1:
                res.append(max(temp))
                print temp
        else:
            temp.pop(0)
            temp.append(arr[i])
            print temp, " - -"
            res.append(max(temp))
    return res

def mytrick(arr,k):
    res= []
    temp = [0]*k
    for i in range(len(arr)):
        temp.append(arr[i])
        if len(temp)==k+1:
            temp.pop(0)
        if len(temp)== k:
            res.append(max(temp))
    return res
        



def bestOne(arr, k):
    from collections import deque
    res= []
    bigger = deque()
    for i , n in enumerate(arr):
        while bigger and arr[bigger[-1]]<=n:
            bigger.popleft()
        bigger += [i]
        if i-bigger[0]>= k:
            bigger.pop()
        
        if i+1>=k:
            res.append(arr[bigger[0]])
    return res




arr = [1,3,-1,-3,5,3,6,7]
k=3
# arr = [1,-1]
# k =1
print maxSlidingWindow(arr, k)
# print mytrick(arr, k)
print bestOne(arr, k)