# def partition(arr, l, h):
#     i = l-1
#     p = arr[h]
#     for j in range(l, h):
#         if arr[j] < p:
#             i += 1
#             arr[j], arr[i]= arr[i], arr[j]
#     arr[i+1], arr[h]=arr[h], arr[i+1]
#     return i+1



# def qsort(arr, low, high):
#     if low<high:
#         p = partition(arr, low, high)

#         qsort(arr, low, p-1)
#         qsort(arr, p+1, high)
class Solution(object):
    def sortArray(self, nums):
        res =[]
        
        res = self.sorta(nums, 0, len(nums)-1)
        print res, "==", nums
        return res
    
    def sorta(self, arr, l, h):
        if l<h:
            p= self.partition(arr, l, h)
            
            self.sorta(arr, l, p-1)
            self.sorta(arr, p+1, h)
        # return arr
            
    def partition(self, arr, l, h):
        i = l-1
        p = arr[h]
        for j in range(l, h):
            if arr[j] < p:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1], arr[h] = arr[h], arr[i+1]
        return i+1




# arr = [5,2,3,1]
# a =Solution()
# a.sortArray(arr)
# print arr

# qsort(arr, 0, len(arr)-1)
# print(arr)


def canConstruct(ransomNote, magazine):
    for i in list(ransomNote):
        if magazine.count(i) < ransomNote.count(i):
          return False
    return True

"bjaajgea"
"affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"
ransomNote = "bjaajgea"
magazine = "affhiiicabhbdchbidghccijjbfjfhjeddgggbajhidhjchiedhdibgeaecffbbbefiabjdhggihccec"

# print canConstruct(ransomNote, magazine)

def cs(n):
    dp = [0] * (n)
    dp[0] = 1
    dp[1] = 2
    print dp
    for i in range(2, n):
        dp[i] = dp[i-1] +dp[i-2]
    print dp
    return dp[n-1]


# print cs(4)


def ispalin(s):
    if len(s) == 1:
        return True
    a= list(s)
    l = 0
    h = len(a)-1
    print a
    while(l<h):
        if not (a[l].isalnum()):
            l = l+ 1
        if not (a[h].isalnum()):
            h = h-1
        if a[l].isalpha() and a[h].isalnum():
            if a[l].lower() != a[h].lower():
                return False
            if a[l].lower() == a[h].lower():
                l = l+1  
                h = h-1
    return True 


# print (ispalin("A man, a plan, a canal: Panama"))


def isMonotonic(arr):
    dec= True
    inc= True
    for i in range(0, len(arr)-1):
        if arr[i] < arr[i+1]:
            dec = False
        if arr[i]>arr[i+1]:
            inc = False
    return dec or inc
        
            
    return True
# print(isMonotonic(['1', '2', '3', '4']))

def reshape(nums, r, c):
    new = [[0]*c]*r
    print new
    # for i in


nums = [[1,2],[3,4]]
r = 1
c = 4
print(reshape(nums, r, c))





    

