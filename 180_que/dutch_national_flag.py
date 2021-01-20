def arrange(arr):
    l= 0
    m= 0
    h= len(arr)-1
    while(m<=h):
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            m = m+1
            l = l+1
        elif arr[m] == 1:
            m = m+1
        elif arr[m] == 2: 
            arr[m], arr[h] = arr[h], arr[m]
            h = h-1
    return arr

a = [1,2,0]#[0,1,2,0,1,2,0,1,2]

print arrange(a)
# print sort012(a)