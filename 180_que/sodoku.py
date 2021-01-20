# def findEmpty(grid, l):
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if grid[i][j]== 0:
#                 l[0]= i
#                 l[1] =j
#                 return False
#     return True

# def checkRow(grid, r,num):
#     for i in range(9):
#         if grid[r][i] == num:
#             return False
#     return True

# def checkCol(grid, c, num):
#     for j in range(9):
#         if grid[j][c] == num:
#             return False
#     return True

# def checkBox(grid, r, c, num):
#     if r+2 >8 or c+2 >8 :
#         return False
#     for i in range(r, r+2):
#         for j in range(c, c+2):
#             print i,j
#             if grid[i][j] ==num:
#                 return False
#     return True
    
# def checkIsSafe(grid, r,c, num):
#     # print r, c, "--"
#     boxR = r - r%3
#     boxC = c - r%3
#     if boxR >8 and boxC>8:
#         return False
#     return checkRow(grid, r, num) and checkCol(grid, c, num) and checkBox(grid, boxR, boxC, num)

# def sudoku(grid):
#     l =[0,0]
#     if findEmpty(grid, l):
#         print grid
#         return True
#     r = l[0]
#     c = l[1]
#     for num in range(1, 10):
#         if checkIsSafe(grid, r, c, num):
#             grid[r][c] = num
#             if sudoku(grid):
#                 return True
#             grid[r][c] = 0
#     return False

# grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
#         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
#         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
#         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
#         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
#         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
#         [0, 0, 5, 2, 0, 6, 3, 0, 0]] 

# print sudoku(grid)

def solveSudoku(board):
	# Check if digit can be placed at position (i,j)
	def is_valid(digit, i, j):
		# check row
		for y in range(len(board)):
			if board[i][y] == str(digit):
				return False
		# check column
		for x in range(len(board)):
			if board[x][j] == str(digit):
				return False
		# check square
		square_x, square_y = i/3, j/3
		for x in range(square_x*3, square_x*3+3):
			for y in range(square_y*3, square_y*3+3):
				if board[x][y] == str(digit):
					return False
		return True

	# Find a valid digit for position (i, j), if possible, and recurse / backtrack
	def search(i, j):
		if i == len(board):
			return True
		elif j == len(board):
			return search(i+1, 0)
		if board[i][j] == ".":
			for digit in range(1, 10):
				if is_valid(digit, i, j):
					board[i][j] = str(digit)
					if search(i, j+1): 
						return True
					board[i][j] = "."
			return False
		else:
			return search(i, j+1)

	search(0,0)
	return board

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
        [5, 2, 0, 0, 0, 0, 0, 0, 0], 
        [0, 8, 7, 0, 0, 0, 0, 3, 1], 
        [0, 0, 3, 0, 1, 0, 0, 8, 0], 
        [9, 0, 0, 8, 6, 3, 0, 0, 5], 
        [0, 5, 0, 0, 9, 0, 6, 0, 0], 
        [1, 3, 0, 0, 0, 0, 2, 5, 0], 
        [0, 0, 0, 0, 0, 0, 0, 7, 4], 
        [0, 0, 5, 2, 0, 6, 3, 0, 0]] 


print solveSudoku(grid)
