def dfs(grid, r, c, visited):
    if r>=len(grid) or r< 0 or c >= len(grid[r]) or c<0 or visited[r][c] or grid[r][c] =="0":
        return 0
    visited[r][c] = 1
    dfs(grid, r+1, c, visited)
    dfs(grid, r, c+1, visited)
    dfs(grid, r-1, c, visited)
    dfs(grid, r, c-1, visited)
    return 1



def noOfIsland(grid):
    res = 0 
    visited = [[0]*len(grid[0]) for _ in range(len(grid))]   
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]=="1" and not visited[i][j]:
                res = dfs(grid, i, j, visited) +res
    return res


grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
# grid = [[1, 1, 0, 0, 0], 
#         [0, 1, 0, 0, 1], 
#         [1, 0, 0, 1, 1], 
#         [0, 0, 0, 0, 0], 
#         [1, 0, 1, 0, 1]] 

print (noOfIsland(grid))