class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def zigzag(root):
    if root is None:
        return 
    q = [root]
    res, temp, flag= [], [], 1
    while q:
        size = len(q)
        for i in range(size):
            curr = q.pop(0)
            temp.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        if not flag:
            res = res + [temp[::-1]]
            flag = True
            temp = []

        else:
            res = res + [temp]
            temp =[]
            flag = False
    return res
    

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)

tree.left.left = Node(4)
tree.left.right = Node(5)

tree.right.left = Node(6)
tree.right.right = Node(7)

tree.left.left.left = Node(10)
tree.left.left.right = Node(11)
tree.left.right.left = Node(12)
tree.left.right.right = Node(13)

tree.right.left.right = Node(15)
tree.right.right.left = Node(16)
tree.right.left.left = Node(14)
tree.right.right.right = Node(17)


#             1
#      2            3
#   4      5      6    7
# 10  11  12 13 14 15 16 17
print zigzag(tree)