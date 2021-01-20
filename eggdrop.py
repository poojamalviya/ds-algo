def eggDrop(n, k):
    if k ==1 or k==0:
        return k
    if n == 1:
        return k
    
    min = 100

    for x in range(1, k+1):
        res = max(eggDrop(n-1, x-1), eggDrop(n, k-x))

        if (res < min):
            min = res
    

    return min+1




n = 5
k = 5

print(eggDrop(n, k))

