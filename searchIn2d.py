def searchMatrix(matrix, target):
    for i in range(0, len(matrix)):
        print i
        if target > matrix[i][0] and target < matrix[i][len(matrix[i])-1]:
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == target:
                    return True
    
    
    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 3

print searchMatrix(matrix, target)