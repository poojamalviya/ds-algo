
n = 8 

def isSafe(x, y ,board):
    if(x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1): 
        return True
    return False
   

def solveKT():
    board  = [[-1 for i in range(n)] for i in range(n)]

    board[0][0]=0

    pos = 1

    if ktUtil(board, 0, 0, pos):
        print(board)
    else:
        print ("doesnot exist")
    return
  
def ktUtil(board, curX, curY, pos):
    if (pos == n**2):
        return True

    moveX=  [2, 1, -1, -2, -2, -1, 1, 2] 
    moveY = [1, 2, 2, 1, -1, -2, -2, -1] 

    for i in range(n):
        newX = curX + moveX[i]
        newY = curY + moveY[i]
        if isSafe(newX, newY, board):
            board[newX][newY]= pos
            if ktUtil(board, newX, newY, pos+1):
                return True
            board[newX][newY] = -1

    return False

solveKT()



