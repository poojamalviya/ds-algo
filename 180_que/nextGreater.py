def nextGreaterEle(arr):
    res=[0]*len(arr)
    stack =[]
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1]<arr[i]:
            stack.pop()
        if not stack:
            res[i] =-1
        else:
            res[i]= stack[-1]
        stack.append(arr[i])
    return res
arr =[98, 23, 54, 12, 20, 7, 100]
print "next greater: ", nextGreaterEle(arr)

def nextSmaller(arr):
    res = [0]*len(arr)
    stack =[]
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1]>arr[i]:
            stack.pop()
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res


print "next smaller: ",  nextSmaller(arr)

def rearrangeArr(arr):
    res = []
    l= 0
    r = len(arr)-1
    while l<r:
        res.append(arr[l])
        l +=1
        res.append(arr[r])
        r -=1
    return res

arr = [1,2,3,4,5,6]

# print rearrangeArr(arr)
