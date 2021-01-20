def findDisappearedNumbers(nums):
    res =[]
    for i in range(0, len(nums)):
        if nums[abs(nums[i])-1]>0:
            print nums[abs(nums[i])-1], nums[i]-1
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
    print(nums)
    
    for i in range(0, len(nums)):
        if nums[i] > 0:
            res.append(i+1)
    return res
        
arr = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(arr))

