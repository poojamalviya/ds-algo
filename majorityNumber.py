# BOYER MOORE voting algorith

def majorityEle(arr):
    majorityEle =0
    count =0
    for i in range(0, len(arr)):
        if count == 0:
            majorityEle = arr[i]
        if majorityEle == arr[i]:
            count += 1
        else:
            count -= 1
    return majorityEle

arr = [2,2,1,1,1,2,2]

print (majorityEle(arr))