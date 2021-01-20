class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.left)
        print root.data,
        inorder(root.right)


# def inorderSuccessor(root):



myTree = Tree(20)
myTree.left = Tree(10)
myTree.right = Tree(30)
myTree.left.left = Tree(5)
myTree.left.right = Tree(15)
myTree.right.right = Tree(35)
myTree.right.left = Tree(25) 

inorder(myTree)

#inorder = left root right 5 10 15 20 25 30 35
#preorder = root left right
#postorder = left right root 

#    BST

#                  20
#               10     30
#             5   15  25  35