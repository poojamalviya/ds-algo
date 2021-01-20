def xorit(arr):
    diff =0
    print arr
    for num in arr:
        diff ^= num
    diff &= -diff #diff & (diff - 1) ^ diff
    a,b =0,0
    for num in arr:
        if num & diff:
            a ^= num
        else:
            b ^= num 
    return a,b

arr = [1,2,1,3,2,5]

print xorit(arr)