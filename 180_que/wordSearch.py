def dfs(board, i, j, word, index):
    if i<0 or j<0 or j>= len(board[0]) or i>= len(board) or board[i][j]==-1 or board[i][j] != word[index]:
        return False
    if len(word)-1==index:
        return True
    visited= board[i][j]
    board[i][j] = -1
    res = dfs(board, i+1, j, word, index+1) or dfs(board, i-1, j, word, index+1) or dfs(board, i, j+1, word, index+1) or dfs(board, i, j-1, word, index+1)
    board[i][j] = visited
    return res

def wordSearch(board, word):
    m = len(board)
    n = len(board[0])
    # visited = [[0]*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if board[i][j]== word[0]:
                if dfs(board, i, j, word, 0):
                    print "here"
                    return True
    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
# board = [["C","A","A"],
#         ["A","A","A"],
#         ["B","C","D"]]
print wordSearch(board, "ABCCED")
print wordSearch(board, "SEE")
# print wordSearch(board, "ABCB")
# print wordSearch(board, "AAB")
