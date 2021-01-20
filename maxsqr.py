# def maxSqur(g):
#     if len(g) == 0:
#         return 0

#     m,n  = len(g), len(g[0])
#     dp = [[0]*(m+1)  for i in range(n+1)]
#     res= 0
#     for i in range(0, m):
#         for j in range(0, n):
#             if i -1> 0 and j-1> 0 and g[i-1][j-1] == 1:
#                 dp[i][j]= min(min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) +1
#                 res = max(res, dp[i][j])
#             else:
#                 if g[i][j] == 1:
#                     dp[i][j]=1
#                     res = max(res, dp[i][j])
#                 else:
#                     dp[i][j]= 0
#     return res*res

def maxSqur(matrix):
    if matrix is None or len(matrix) < 1:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    dp = [[0]*(cols+1) for _ in range(rows+1)]
    max_side = 0
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 1:
                dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                max_side = max(max_side, dp[r+1][c+1])
    print dp, 
            
    return max_side * max_side


# g= [[1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0]]

g = [[1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]]
# g = [[1]]
print maxSqur(g)