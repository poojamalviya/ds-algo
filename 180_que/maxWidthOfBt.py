class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def getMaxWidth(root):
    width =0
    q = [(root, 1)]
    while q:
        size = len(q)
        for i in range(size):
            curr = q.pop(0)
            node, index= curr[0], curr[1]
            if node.left:
                q.append((node.left, index*2))
            if node.right:
                q.append((node.right, index*2+1))
        if q:
            width = max(width, q[-1][1]-q[0][1]+1)
    return width


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.right = Node(8) 
root.right.right.left = Node(6) 
root.right.right.right = Node(7)

# print getMaxWidth(root)

print getMaxWidth(root)

#        1 
#       / \ 
#      2   3 
#     / \   \ 
#    4   5   8  
#           / \ 
#          6   7 