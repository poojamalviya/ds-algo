def binarySearch(arr, t):
    aa= binary(arr, 0, len(arr)-1, t)
    return aa

def  binary(arr, l, h, t):
    if h>=l:
        mid =  l+h-l/2
        if arr[mid] == t:
            return mid
        elif arr[mid] >t :
            return binary(arr, l, mid-1, t)
        else:
            return binary(arr, mid+1, h, t)  
    else:
        return -1

arr =[5]
t = 5

# print(binarySearch(arr, t))

def reverse(a):
    s = a.split(' ')
    res, rev = '', '' 
    for word in s:
        for letter in range(len(word)-1, -1, -1):
            rev = rev + word[letter]
        res = res + " " + rev
        rev =''
    print res


# reverse("Let's take LeetCode contest")
# A-Z = 65-90
# a-z = 97-122
def small(w):
    w = list(w)
    for i in range(0, len(w)):
        if ord(w[i]) <=90 and ord(w[i]) >= 65:
            index = ord(w[i]) - 65
            w[i] = chr(int(97+index))
    return "".join(w)

# print small("al&phaBET")

def findDuplicates(nums):
    res = []
    
    for item in nums:
        if nums[abs(item) - 1] < 0:
            res.append(item)
        else:
            nums[item - 1] = - nums[item - 1]
    
    
    return res

# findDuplicates([4,3,2,7,8,2,3,1])
def mainfun(arr):
    total = 0
    total = sum(i*arr[i] for i in arr)
    print total



mainfun([1,2,3,4])
