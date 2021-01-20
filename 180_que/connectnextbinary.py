class newnode: 
    def __init__(self,data): 
        self.data = data  
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if not root:
        return 
        
    while curr:

  
# Constructed binary tree is  
#       10  
#      / \  
#    8     2  
#   /        \  
#  3         90  
root = newnode(10)  
root.left     = newnode(8)  
root.right     = newnode(2)  
root.left.left = newnode(3)  
root.right.right     = newnode(90)  

# Populates nextRight pointer in all nodes  
connect(root)  