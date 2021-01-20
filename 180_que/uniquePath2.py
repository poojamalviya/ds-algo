def uniquePath(grid):
    for i in range(1,len(grid)):
        for j in range(1, len(grid[0])):
            if i ==0 or j==0:
                continue
            elif grid[i][j]==1:
                grid[i][j]=0
            elif i==0:
                grid[i][j]= 1+ grid[i][j-1]
            elif j==0:
                grid[i][j] = 1+ grid[i-1][j]
            else:
                grid[i][j] = grid[i-1][j]+grid[i][j-1]
    print grid
    return grid[-1][-1]
            


grid =[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
# grid = [[0,1]]
# Output: 2

print uniquePath(grid)