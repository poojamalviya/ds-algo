def isLandPrimer(arr):
    row = len(arr)
    col = len(arr[0])
    island =0
    neighbour =0
    for i in range(row):
        for j in range(col):
            if arr[i][j]==1:
                island = island+1
                if i+1<row and arr[i+1][j] ==1:
                    neighbour=neighbour+1
                if j+1<col and arr[i][j+1]==1:
                    neighbour = neighbour+1
    return island*4 - neighbour*2

arr =[[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]

print isLandPrimer(arr)