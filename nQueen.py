N=4

def isSafe(board, row, col):
    for i in range (col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    if col >=N:
        return True
    
        for i in range(N):
            if isSafe(board, i , col):
                board[i][col] = 1
                if solveNQUtil(board, col+1):
                    return True
                
                board[i][col]= 0
        return False

def solveNQ(): 
    board = [ [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0], 
              [0, 0, 0, 0] ] 
  
    if solveNQUtil(board, 0) == True: 
        print (board)

    print ("Solution does not exist") 
    return True
  
# Driver Code 
solveNQ() 