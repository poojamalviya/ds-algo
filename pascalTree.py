#        1          0  0
#      1   1        2  1
#     1  2   1      3  2
#    1 3   3  1     4  3
#   1  4  6  4 1    5  4
#  1  5  10 10 5 1  6  5
# 1 6 15  20  15 6 1 7 6

def pascalTree(n):
    prevTree =[]

    if n ==0:
        prevTree = [1]
    if n == 1 :
        prevTree = [1, 1]

    prevTree = [1] * (n+1)

    for _ in range(0, n):
        print prevTree , _
        for i in range(0, n):
            if i+1 < n:
                nexte = prevTree[i] + prevTree[i+1]
                prevTree[i] = nexte
        
    return prevTree
print(pascalTree(3))



