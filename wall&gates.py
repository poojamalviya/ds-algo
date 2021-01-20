def wallAndGates(rooms):
    for i in range(0, len(rooms)):
        for j in range(i, len(rooms[i])):
            if rooms[i][j] == 0:
                dfs(i, j, 0, rooms)

def dfs(i, j, count, rooms):
    if(i<0 or i >= len(rooms) or j<0 or j>=len(rooms[i]) or rooms[i][j]< count):
        return
    
    rooms[i][j] = count
    dfs(i+1, j, count+1, rooms)
    dfs(i, j+1, count+1, rooms)
    dfs(i-1, j, count+1, rooms)
    dfs(i, j-1, count+1, rooms)


rooms= [[100, -1, 0, 100],
        [100, 100, 100, -1],
        [100, -1, 100, -1],
        [0, -1, 100, 100]]

wallAndGates(rooms)
print rooms
