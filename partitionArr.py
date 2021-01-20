# Example 1:
def partition(arr):
    suma = 0
    for i in range(0, len(arr)):
        suma += arr[i]
    reminder  = suma%3
    if reminder !=0:
        return False
    total = suma//3
    print suma, total
    local =0
    c = 0
    for i in range(0, len(arr)):
        local +=  arr[i]
        if arr[i] != 0:
            if i == len(arr)-1:
                print (i, len(arr)-1)
                print local,total
                if local != total:
                    return False
            if total == local and c !=2 :
                print i
                local = 0
                c += 1
    return True
        
    
    


arr =  [0,2,1,-6,6,-7,9,1,2,0,1] #[12,-4,16,-5,9,-3,3,8,0]
print(partition(arr))
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# Example 2:

# Input: 
# Output: false
# Example 3:

# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4