

def subset():
    s = [1,2,3]
    res =[]
    count =0
    while count < len(s):
        arr =[]
        for i in range(0, count):
            arr.append(s[i])

        res.append(arr)
        count = +1
    return res





print(subset())