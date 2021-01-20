def longest_increasing_subsequence(arr):
    if len(arr) == 1:
        return 1
    max_ending = 0
    for i in range(len(arr)):
        till_here = longest_increasing_subsequence(arr[:i])
        if arr[-1] > arr[i-1] and till_here +1 > max_ending:
            max_ending= till_here +1
    return max_ending


def lic_dp(arr):
    myarr = [1] * len(arr)
    
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i]> arr[j]:
                myarr[i] = max(myarr[i], myarr[j]+1)
    print myarr
    return max(myarr)

arr= [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

# print(longest_increasing_subsequence(arr))
print(lic_dp(arr))