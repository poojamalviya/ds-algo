
def porusWall(grid, m, n):
    r = 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if (i+1 < m and j-1>=0 and i+1 < m and j+1 < n):
                    if grid[i+1][j-1] or grid[i+1][j+1] or grid[i+1][j]:
                        r += 1
                    else:
                        return False
    return True if r==m else False

    



grid = [[0,0,0,1,0],
        [0,0,1,0,0],
        [0,0,1,0,0], 
        [0,1,0,0,0], 
        [0,0,1,0,0],
        [0,0,1,1,0]]

m = len(grid)
n = len(grid[0])
print porusWall(grid, m, n)