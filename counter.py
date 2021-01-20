from collections import Counter

def uniqueNumberOccurance(arr):
    pp= Counter(arr)
    let = []
    for key in pp:
        print key
        if pp[key] not in let:
            let.append(pp[key])
        else:
            return False
    return True


arr = [1,2,2,1,1,3]
# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# arr = [1,2]

# print(uniqueNumberOccurance(arr))



def reform(arr):
    if len(arr)== 0:
        return None
    counter = 0
    index = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            counter = counter+2
        else:
            counter = counter +1
        if len(arr) == counter:
            index = i
            break
    for j in range(len(arr)-1, -1, -1):
        if arr[j] == 0:
            arr[j-1] = 0
            c = c+1
        else:
            arr[j+c] = arr[index]
            index = index-1
        j = j+c
    return arr
            
arr = [1,0,2,3,0,4,5,0]
print reform(arr)
