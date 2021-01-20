def isSafe(board, r, c):
    for i in range(c):  # check left side of row
        if board[r][i]:
            return False
    i = r   # check upper left diagonal
    j= c
    while(i>= 0 and j>=0):
        if board[i][j]:
            return False
        i = i-1
        j = j-1
    i = r # check lower left diagonal
    j= c
    while(i<len(board) and j>=0):
        if board[i][j]:
            return True
        i = i+1
        j =j-1
def nQueen(board, col):
    if len(board[0])==col:
        return True
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1
            if nQueen(board, col+1):
                return True
            board[row][col] =0
    return False

board = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 
nQueen(board, 0)
