def levelOrderTraversal(root):
    res = []
    q = []
    q.append(root)
    while q:
        size = len(q)
        temp = []
        for i in range(size):
            curr = q.pop(0)
            temp.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        res.append(temp)
    return res[::-1]


        

# [
#   [15,7],
#   [9,20],
#   [3]
# ]
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

root = Node(3) 
root.left = Node(9) 
root.right = Node(20) 
root.left.left = Node(15) 
root.left.right = Node(7) 

print levelOrderTraversal(root)