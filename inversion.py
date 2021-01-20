
def mergeSort(arr, tempArr, low, high):
    inv = 0
    if low < high :
        mid = (low +high) // 2
    
        inv =  mergeSort(arr, tempArr, low, mid)
        inv += mergeSort(arr, tempArr, mid+1, high)
        inv += merge(arr, tempArr, low, mid, high)
    return inv

def merge(arr, tempArr, l, m , r):
    i =l
    j =m+1
    k = l
    inv_count =0
    while i <= m and j <= r:
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            k = k+1
            i = i+1
        else:
            tempArr[k] = arr[j]
            k = k+1
            j =j+1
            inv_count += m-i +1
    while i<= m :
        tempArr[k] = arr[i]
        k= k+1
        i = i +1
    while j<= r :
        tempArr[k] = arr[j]
        k =k+1
        j = j+1

    for m in range(l,r+1):
        arr[m] = tempArr[m]
    return inv_count


arr = [1, 20, 6, 4, 5] 
n = len(arr)

tempArr = [0] *n

print (mergeSort(arr, tempArr, 0, n-1))


