def pascal(n):
    res =[]
    for i in range(n):
        temp = [None for i in range(i+1)]
        temp[0], temp[-1] =1,1
        for k in range(1, len(temp)-1):
            temp[k] = res[i-1][k-1]+res[i-1][k]
        res.append(temp)
    return res

print pascal(4)


