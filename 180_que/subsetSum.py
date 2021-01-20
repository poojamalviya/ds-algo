def subsetsgeneral(arr):
    res=[]
    subsetrec(arr, 0,[], res)
    return res
def subsetrec(arr, index, temp, res):
    if len(arr)==index:
        res.append(temp)
        return 
    temp = temp+[arr[index]]
    subsetrec(arr, index+1, temp, res)
    subsetrec(arr, index+1, temp[:-1], res)
    

def findSubsetsRec(arr, n, currSet, sum, res) :
    import time
    time.sleep(1)
    if sum == 0:  
        res.append(currSet)
        return
    if(n == 0):
        return
    findSubsetsRec(arr, n - 1, currSet, sum, res) #recursion
    print currSet, "curr - - "
    currSet = [] + currSet
    print currSet, " - -"
    currSet.append(arr[n - 1]) 
    findSubsetsRec(arr, n - 1, currSet, sum - arr[n - 1], res)  #backtracting 

#main function
def findSubsets(_arr, n, sum):
    res = []
    currSet = []
    findSubsetsRec(arr, n, currSet, sum, res)
    return res


# Driver code 
arr = [10,1,2,7,6,5]
sum = 8
n = len(arr) 
print findSubsets(arr, n, sum) 

num= [1,2,3,4]
print subsetsgeneral(num)


# here i am using recursion and backtracting to find all the subarray of target sum in an array.
# complexity of the solution is 2 to the power n where n is the number of element in array as one by one we are checking all 
# possible subarray sum if they are equal to the target number




# a = [1,2,4,7,9,11]
# t = 11
# print subsets(a, t)

# [[4,7], [9,2], [11]]