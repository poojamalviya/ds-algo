
def __init__(self, key):
    self.data =key
    self.left = None
    self.right = None

import q from Queue
def sumDifference(root):
    if root None:
        return 0

    q = q.Queue
    q.add(root)
    q.add("*")

    level = 0
    evenSum = 0
    oddSum = 0

    while(q.size()>0):
        curr = q.pop()
        if curr == "*":
            level +=1
            curr = q.pop()
            if curr.left or curr.right:
                q.add("*")
        if level %2:
            evenSum = evenSum + curr.data
        else:
            oddSum = oddSum + curr.data
        
        if curr.left:
            q.add(curr.left)
        if curr.right:
            q.add(curr.right)
        

    return abs(evenSum-oddSum)

    
queue = [1, *, 2, 3, *, 4, 5, 6, 7, *, 8,9, *]

#           1 *
#         /   \
#       2      3 *
#    /   \   /  \
#   4     5  6    7 
#  / \
# 8  9