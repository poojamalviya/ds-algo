class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traverse(tree):
    if tree is None:
        return 
    if tree.left:
        inorder_traverse(tree.left)
    
    print tree.data

    if tree.right:
        inorder_traverse(tree.right)

    
def preorder_traverse(tree):
    if tree is None:
        return 
    print tree.data

    if tree.left:
        preorder_traverse(tree.left)
    if tree.right:
        preorder_traverse(tree.right)

def post_traverse(tree):
    if tree is None:
        return 
    if tree.left:
        post_traverse(tree.left)
    if tree.right:
        post_traverse(tree.right)
    print tree.data


def height(tree):
    if tree is None:
        return 0
    l_height = 1 + height(tree.left)
    r_height = 1 + height(tree.right)
    if l_height > r_height:
        return l_height
    else:
        return r_height

def leaf(tree, arr):
    if tree is None:
        return 
    if tree.right is None and tree.left is None:
        arr.append(tree.data)
        return
    if tree.left:
        leaf(tree.left, arr)
    if tree.right:
        leaf(tree.right, arr)

def printLeafs(tree):
    if tree is None:
        return
    arr = []
    leaf(tree, arr)
    print arr

def level_order(tree):
    if tree is None:
        return
    q = []
    q.append(tree)
    while q :
        ele = q.pop(0)
        print ele.data,
        # print q[0].data, 
        # ele = q.pop(0) 

        if ele.left is not None:
            q.append(ele.left)
        if ele.right is not None:
            q.append(ele.right)

def level_print(tree):
    if tree is None:
        return
    q=[]
    q.append(tree)
    q.append('*')
    while q:
        if q[0] is "*":
            print '\n'
            q.pop(0)
            q.append("*")

        print q[0].data,
        ele = q.pop(0)
        if ele.left:
            q.append(ele.left)
        if ele.right:
            q.append(ele.right)


import Queue 
def bottomLeftView(root):
    q = Queue.Queue()
    q.put(root)

    while(not q.empty()):
        curr = q.get()
        if curr.right != None:
            q.put(q.right)
        if curr.left != None:
            q.put(q.left)
    return curr.val
 
def leftView(root):
    q = Queue.Queue()
    q.put(root)
    q.put("*")

    while(not q.empty()):
        curr = q.get()
        # print curr.data
        if curr == "*":
            q.get()
            curr = q.get()
            print curr.data
            q.put("*")
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)

def rightviewRec(root, max_level, level):
    print level,
    if root is None:
        return 
    if max_level>level[0]:
        print root.data
        level[0] = max_level
    rightviewRec(root.right, max_level+1, level)
    rightviewRec(root.left, max_level+1, level)


def rob(root):
    if root is None:
        return 
    evenSum = 0
    oddSum = 0
    l = 0
    import Queue
    q = Queue.Queue()
    q.put(root)
    # print root.data
    while(not q.empty()):
        currSum = 0
        s = q.qsize()
        # print s, 's'
        if l%2 ==0:
            evenSum = currSum + evenSum
        else:
            oddSum = oddSum +currSum
        l += 1
        for i in range(0, s):
            curr = q.get()
            print curr.data
            currSum = currSum + curr.data
            
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)
        
    return max(evenSum, oddSum)


import time
def connect(root):
    if root is None:
        return 
    res =[]
    import Queue
    q = Queue.Queue()
    q.put(root)
    while (not q.empty()):
        time.sleep(1)
        s = q.qsize()
        # print curr.data
        for i in range(0, s):
            print s
            print res
            curr = q.get()
            res.append(curr.data)
            if s-1 == i:
                res.append("#")
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
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


# inorder_traverse(tree)
# preorder_traverse(tree)
# post_traverse(tree)
# print height(tree)
# printLeafs(tree)
# level_order(tree)
# level_print(tree)

# print(bottomLeftView(tree))
# leftView(tree)
# rightviewRec(tree, 0+1, [0])
# rob(tree)
print connect(tree)