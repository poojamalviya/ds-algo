import time
def maxPathSum(grid, m,n):
    print m,n
    time.sleep(1)
    print grid
    if m==0 and n == 0:
        return grid[m][n]
    if m==0: return grid[m][n] + min(maxPathSum(grid, m, n-1))
    if n==0: return grid[m][n] +min(maxPathSum(grid,m-1,n))
    return grid[m][n] +min(maxPathSum(grid, m-1, n), maxPathSum(grid, m, n-1))

# def minPathSum(grid):
#     c = len(grid)
#     r = len(grid[0])    
#     for i in range(c):
#         for j in range(r):
#             if i ==0 and j ==0:
#                 continue
#             elif i == 0:
#                 grid[i][j] += grid[i][j-1]
#             elif j == 0:
#                 grid[i][j] += grid[i-1][j]
#             else:
#                 grid[i][j] += min(grid[i][j-1], grid[i-1][j])
#     print grid
#     return grid[-1][-1]
def minPathDP(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i ==0 and j ==0:
                continue
            elif i==0:
                grid[i][j] += grid[i][j-1]
            elif j==0:
                grid[i][j] += grid[i-1][j]
            else:
                grid[i][j] +=min(grid[i][j-1], grid[i-1][j])
    print grid
    return grid[-1][-1]
            
grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
# [[1, 4, 5], 
# [2, 7, 6], 
# [6, 8, 7]]

# Output: 7
print minPathDP(grid)
# print maxPathSum(grid, len(grid), len(grid[0]))
# print minPathSum(grid)