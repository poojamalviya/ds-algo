def  permute(a, l, r):
    if l== r:
        print(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

s= "abc"
slen = len(s)
arr= list(s)
permute(arr, 0 , slen)

