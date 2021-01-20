class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None

def topView(root, myhash, key):
    if root is not None:
        if key not in myHash: 
            myHash[key] = root.data
            topView(root.left, myhash, key-1)
            topView(root.right,myhash, key+1)
    # return myHash

def topViewInSequence(root):
    if root is not None:
        q = []
        q.append(root)
        h = dict()
        k = 0
        while len(q) >0:
            n = q[0]
            if k not in h:
                print k , 'k'
                h[k] = n.data
            if n.left:
                q.append(n.left)
                k = k-1
            if n.right:
                q.append(n.right)
                k = k+1
            q.pop(0)
        print h
        for i in h:
            print h[i]




myTree = Node(1)
myTree.left= Node(2)
myTree.right= Node(3)
myTree.left.left= Node(4)
myTree.left.right = Node(5)
myTree.right.left= Node(6)
myTree.right.right = Node(7)
myTree.left.right.right = Node(9)

myHash = dict()

# print (topView(myTree, myHash, 0))
# print myHash
topViewInSequence(myTree)
#          1
#       2      3
#    4    5   6    7
#          9