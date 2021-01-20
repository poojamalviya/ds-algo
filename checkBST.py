class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def checkBst(root):
    if not root.data:
        return True

    print(bstUtil(root, None, None))
    

# def bstUtil(root, l=None, r=None):
#     if root is None:
#         return True
    
#     if (l!= None and root.data <= l.data):
#         return False
#     if (r!= None and root.data >=r.data):
#         return False
    
#     return bstUtil(root.left, l, root) and bstUtil(root.right, root, r)

def bstUtil(root, l = None, r = None):  
  
    if (root == None) : 
        return True

    if (l != None and root.data <= l.data) : 
        return False
  
    if (r != None and root.data >= r.data) : 
        return False
   
    return bstUtil(root.left, l, root) and bstUtil(root.right, root, r)  
  

tree = Node(50)
tree.left = Node(25)
tree.right = Node(55)

tree.left.left = Node(10)
tree.left.right = Node(15)

tree.right.left = Node(60)
tree.right.right = Node(52)

checkBst(tree)
