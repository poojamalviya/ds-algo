class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def boundaryElement(root):
    if root is not None:
        left(root)
        bottom(root)
        right(root)


def left(root):
    if root.left:  
        print root.data
        left(root.left)
    elif root.right:
        print root.data
        left(root.right)

def right(root):
    if root.right:
        print root.data
        right(root.right)
    elif root.left:
        print root.data
        right(root.left)

def bottom(root):
    if root is not None:
        if root.right is None and root.left is None:
            print root.data
        if root.left:
            bottom(root.left)
        if root.right:
            bottom(root.right)
    

def boundaryView(root):
    import Queue
    q =Queue.Queue()
    q.put(root)
    res={}
    c =0
    while(not q.empty()):
        curr = q.get()
        print curr
        if curr.left:
            q.put(curr.left)
            res[c-1]= curr.left
        if curr.right:
            q.put(curr.right)
            res[c+1]=curr.right
    print c



myTree = Node(1)
myTree.left= Node(2)
myTree.right= Node(3)
myTree.left.left= Node(4)
myTree.left.right = Node(5)
myTree.right.left= Node(6)
myTree.right.right = Node(7)
myTree.left.right.right = Node(9)

# boundaryElement(myTree)
boundaryView(myTree)

#          1
#       2      3
#    4    5   6    7
#          9