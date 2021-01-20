def dfs(v, r, c):
    cr = [-1, -1, -1,  0, 0,  1, 1, 1]
    cc = [-1,  0,  1, -1, 1, -1, 0, 1]
    v[r][c]= True
    for k in range(8):
        if isSafe( r + cr[k], c + cc[k], v):
            dfs(r+ cr[k], c+ cc[k], v)


def isSafe(r, c, v):
    if r <8 and r >0 and c <8 and c> 0 and v[r][c] == False:
        return True


def noOfIsland(graph, r, c):
    visited = [[False for j in range(r)] for i in range(c)]
    count = 0

    for i in range(r):
        for j in range(c):
            if visited[i][j] is False and graph[i][j] == 1:
                dfs(visited, i, j)
                count += 1
    return count











graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 

print (noOfIsland(graph, 5, 5))