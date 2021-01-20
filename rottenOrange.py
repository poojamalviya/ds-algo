import Queue
import time
def rottenOrange(grid):
    r = len(grid)
    c = len(grid[0])
    q = Queue.Queue()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                q.put((i,j))
    q.put((-1, -1))
    res=0
    while not q.empty():
        time.sleep(1)
        i, j = q.get()
        print i,j
        if i == -1 and j == -1:
            res += 1
            q.put((-1, -1))
        else:
            if i+1 < r or j+1 < c or i-1>=0 or j-1>=0:
                grid[i+1][j] = 2
                q.put((i+1, j))
                grid[i][j+1] = 2
                q.put((i, j+1))
                grid[i-1][j] = 2
                q.put((i-1, j))
                grid[i][j-1] = 2
                q.put((i, j-1))
    
    print res
    return res

    


grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]


rottenOrange(grid)