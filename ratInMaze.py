N=4
def solveMaze(maze):
    sol =  [[0 for i in range(4)] for i in range(4)]

    if solveUtil(maze, 0, 0, sol):
        print (sol)
    else:
        print ("not found")
    return

def isSafe(maze, x, y):
    if(x >= 0 and y >= 0 and x<N and y<N and maze[x][y]==1):
        return True
    return False

def solveUtil(maze, x, y, sol):
    if (x == N-1 and y == N-1):
        sol[x][y]=1
        return True

    if isSafe(maze, x, y):
        sol[x][y] = 1
        if solveUtil(maze, x+1, y, sol):
            return True
        if solveUtil(maze, x, y+1, sol):
            return True
        sol[x][y]= 0
        return False
    



maze = [ [1, 0, 0, 0], 
            [1, 1, 0, 1], 
            [0, 1, 0, 0], 
            [1, 1, 1, 1] ] 

               
solveMaze(maze) 