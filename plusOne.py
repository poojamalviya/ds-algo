def plusOne(arr):
    s =''
    res = []

    for i in arr:
        s = s + str(i)
    print s

    add = int(s)+1
    for i in str(add):
        res.append(int(i))
    return res




arr= [9, 9]

print(plusOne(arr))