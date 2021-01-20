def setSol(arr):
    s= set()
    for i in arr:
        if i in s:
            return i
        s.add(i)

def sortSol(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]

#not for negative number
def negate(arr):
    for i in range(0, len(arr)):
        if arr[abs(arr[i])]>0:
            arr[abs(arr[i])] = - arr[abs(arr[i])]
        else:
            return abs(arr[i])
    
        
def tortoiseAndhare(arr):
    hare = tortoise = arr[0]
    while (True):
        hare = arr[arr[hare]]
        tortoise = arr[tortoise]
        if hare == tortoise:
            break  

    tortoise = arr[0]
    while (hare != tortoise):
        hare = arr[hare]
        tortoise = arr[tortoise]
    
    return hare




# a = [1,2,3,1,5,4]
# a = [1,3,4,2,2]
a = [3,1,3,4,2]

print setSol(a)
print sortSol(a)
print negate(a)
print tortoiseAndhare(a)
