from collections import Counter
def uncommon(A,B):
    count = {}

    # for word in A.split():
        # count[word] = count.get(word) +1

    a = Counter(A.split())
    a += Counter(B.split())

    return [w for w in a if a.get(w) == 1]


A = "this apple is sweet"
B = "this apple is sour"
# Output: ["sweet","sour"]

# print uncommon(A,B)

def replace(arr):
    arr.append(-1)
    for i in range(len(arr)-1, 0, -1):
        if arr[i] > arr[i-1]:
            arr[i-1] = arr[i]
    
    return arr[1:]

arr = [17,18,5,4,6,1]
print replace(arr)

    