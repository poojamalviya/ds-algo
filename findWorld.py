def wordSearch(board, let):
    for i in range(0, len(board)):
        for j in range(i, len(board[i])):
            if board[i][j] == let[0]:
                if dfs(board,i, j, 0,let):
                    return True

def dfs(board, i,j,count, let):
    print (count, len(let))
    if count == len(let):
        return True
    if (i >=0 and i < len(board) and j >= 0 and j< len(board) and board[i][j]== let[count]):
        temp = board[i][j]
        board[i][j] =" "
        check = dfs(board, i+1, j, count+1, let) or dfs(board, i-1, j, count+1, let) or dfs(board, i, j+1, count+1, let)or dfs(board, i, j-1, count+1, let)
        board[i][j] = temp
        return check 
    return False

    


board =[['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']]

print(wordSearch(board, "ABCCED"))

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
