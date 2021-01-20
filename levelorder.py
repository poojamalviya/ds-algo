class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def levelOder(root):
    if root is None:
        return 
    queue = []
    res, loc =[], []
    queue.append(root)
    queue.append('-')
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr != '-':
            loc.append(curr.data)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        if curr == '-':
            res.append(loc)
            loc = []
            if queue:
                queue.append('-')
   
    print res



#      1
#   2     3
# 4  5  6   7
myTree = Node(1)
myTree.left= Node(2)
myTree.right= Node(3)
myTree.left.left= Node(4)
myTree.left.right = Node(5)
myTree.right.left= Node(6)
myTree.right.right = Node(7)

levelOder(myTree)













# def levelOder(root):
#     if root ==  None:
#         return 
#     else:
#         queue = []
#         queue.append(root)

#         while len(queue)>0:
#             curr = queue.pop(0)
#             print (curr.data)

#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)