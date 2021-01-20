
# def orangesRotting(grid):
#     row, col = len(grid), len(grid[0])
#     res =0
#     rotten =[]
#     rotten = [(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2]
#     fresh = 0
#     for i in range(row):
#         for j in range(col):
#             if arr[i][j]== 1:
#                 fresh = fresh +1
#     while fresh >0 and rotten:
#         res = res+1
#         for index in rotten:
#             i, j = index[0], index[1]
#             rotten.remove(index)
#             for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
#                 if 0<=x<row and 0<=y<col and grid[x][y]==1:
#                     grid[x][y] = 2
#                     fresh= fresh -1
#                     rotten.append((x,y))
#     if fresh>0:
#         return -1
#     return res


# def orangesRotting(arr):
#     res = 0
#     row = len(arr)
#     col = len(arr[0])
#     rotten =[]

#     for i in range(row):
#         for j in range(col):
#             if arr[i][j]== 2:
#                 rotten.append((i,j))
#     fresh =0
#     for i in range(row):
#         for j in range(col):
#              if i ==1 and j ==1:
#                  fresh = fresh+1
#     while  fresh>0 or rotten:
#         print rotten
#         curr = rotten.pop(0)
#         i, j = curr[0], curr[1]
#         for x,y in [(i+1, j), (i,j+1), (i-1,j),(i,j-1)]:
#             if 0<=x<row  and 0<=y<col and arr[x][y] == 1:
#                 rotten.append((x, y))
#                 arr[x][y]=2
#                 fresh= fresh-1
#         res = res+1
#     return res

def orangesRotting(grid):
    row = len(grid)
    col = len(grid[0])
    rotten = [(i,j) for i in range(row) for j in range(col) if grid[i][j] == 2]
    fresh =0
    for i in range(row):
        for j in range(col):
            if grid[i][j]==1:
                fresh = fresh+1
    res =0
    while rotten and fresh>0:
        size = len(rotten)
        for i in range(size):
            print rotten
            curr = rotten.pop(0)
            i, j = curr[0], curr[1]
            for x,y in [(i+1,j), (i,j+1), (i-1,j), (i,j-1)]:
                if 0<=x<row and 0<=y<col and grid[x][y] ==1:
                    rotten.append((x,y))
                    grid[x][y] = 2
                    fresh= fresh-1
        res = res+1
    if fresh>0:
        return -1 
    else:
        return res









arr = [[2,1,1],
       [1,1,0],
       [0,1,1]]
# arr = [[2,1,1],
#         [0,1,1],
#         [1,0,1]]
# arr= [[2,2,2,1,1]]

# print rottenOrange(arr)
print orangesRotting(arr)