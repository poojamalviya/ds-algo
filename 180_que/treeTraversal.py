def inOrder(root):
    res =[]
    stack = []
    curr = root
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            te = stack.pop()
            res.append(te.data)
            curr = te.right
    return res


def preOrder(root):
    res =[]
    stack = [root]
    curr = root
    while len(stack)>0:
        temp = stack.pop()
        print temp.data
        res.append(temp.data)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)
    return res


def postOrder(root):
    res =[]
    stack =[root]
    while stack:
        temp = stack.pop()
        res.append(temp.data)
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
    return res[::-1]
        
    

class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

    #         1 
    #       /   \ 
    #      2     3 
    #    /  \ 
    #   4    5   """

  
# print inOrder(root)  # 4 2 5 1 3  # left root right
# print preOrder(root)  # 1 2 4 5 3  # root left right
print postOrder(root) # 4 5 2 3 1 # left right root