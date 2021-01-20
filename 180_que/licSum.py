def MSIS(A, i, n, prev, sum):
	if i == n:
		return sum
	excl = MSIS(A, i + 1, n, prev, sum)
	incl = sum
	if A[i] > prev:
		incl = MSIS(A, i + 1, n, A[i], sum + A[i])
	return max(incl, excl)


def longestIncreasingRec(arr):
    res=0
    return dfs(arr, 0,-1, 0)
    # return res

def dfs(arr, index, prev, res):
    if len(arr) == index:
        return res
    excl= dfs(arr, index+1, prev, res)
    incl = res
    if prev<arr[index]:
        incl =dfs(arr, index+1, arr[index], res+arr[index])
    return max(excl, incl)


if __name__ == '__main__':

	A = [8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11]
	print("Maximum sum of increasing subsequence is",
		  MSIS(A, 0, len(A), float('-inf'), 0)), longestIncreasingRec(A)



Happay will provide the 
 