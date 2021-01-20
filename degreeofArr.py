# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

arr = [1,2,2,3,1,4,2]



# An array that has degree d, must have some element x occur d times. If some subarray has the same degree, then some element x (that occured d times), still occurs d times. The shortest such subarray would be from the first occurrence of x until the last occurrence.

# For each element in the given array, let's know left, the index of its first occurrence; and right, the index of its last occurrence. For example, with nums = [1,2,3,2,5] we have left[2] = 1 and right[2] = 3.

# Then, for each element x that occurs the maximum number of times, right[x] - left[x] + 1 will be our candidate answer, and we'll take the minimum of those candidates.

# Python

# class Solution(object):
#     def findShortestSubArray(self, nums):
#         left, right, count = {}, {}, {}
#         for i, x in enumerate(nums):
#             if x not in left: left[x] = i
#             right[x] = i
#             count[x] = count.get(x, 0) + 1

#         ans = len(nums)
#         degree = max(count.values())
#         for x in count:
#             if count[x] == degree:
#                 ans = min(ans, right[x] - left[x] + 1)

#         return ans