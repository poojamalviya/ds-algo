


def maxArea(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        if i>=0 and j >=0  and i<m and j<n and grid[i][j]:
            grid[i][j] = 0
            return 1+ dfs(i-1, j) + dfs(i, j-1) + dfs(i+1, j) + dfs(i, j+1)
        return 0

    res =0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                area = dfs(i, j)
                res = max(res, area)
    return res

grid = [[0,1,1,0,1,1,0,0],
        [0,0,1,0,1,1,1,0],
        [0,1,1,0,1,1,1,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
print maxArea(grid)