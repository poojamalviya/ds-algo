from __future__ import print_function
import math

class SegmentTree:

    def __init__(self, A):
        self.N = len(A)
        self.st = [0] * (4 * self.N) # approximate the overall size of segment tree with array N
        self.build(1, 0, self.N - 1)

    def left(self, idx):
        return idx * 2

    def right(self, idx):
        return idx * 2 + 1

    def build(self, idx, l, r):
        if l == r:
            self.st[idx] = A[l]
        else:
            mid = (l + r) // 2
            self.build(self.left(idx), l, mid)
            self.build(self.right(idx), mid + 1, r)
            self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])

    def update(self, a, b, val):
        return self.update_recursive(1, 0, self.N - 1, a - 1, b - 1, val)

    def update_recursive(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if r < a or l > b:
            return True
        if l == r :
            self.st[idx] = val
            return True
        mid = (l+r)//2
        self.update_recursive(self.left(idx), l, mid, a, b, val)
        self.update_recursive(self.right(idx), mid+1, r, a, b, val)
        self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
        return True

    def query(self, a, b):
        return self.query_recursive(1, 0, self.N - 1, a - 1, b - 1)

    def query_recursive(self, idx, l, r, a, b): #query(1, 1, N, a, b) for query max of [a,b]
        if r < a or l > b:
            return -float('inf')
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l+r)//2
        q1 = self.query_recursive(self.left(idx), l, mid, a, b)
        q2 = self.query_recursive(self.right(idx), mid + 1, r, a, b)
        return max(q1, q2)

    def showData(self):
        showList = []
        for i in range(1,N+1):
            showList += [self.query(i, i)]
        print(showList)


if __name__ == '__main__':
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(A)
    print(segt.query(4, 6))
    print(segt.query(7, 11))
    print(segt.query(7, 12))
    segt.update(1,3,111)
    print(segt.query(1, 15))
    segt.update(7,8,235)
    segt.showData()



#     class NumArray:
#     def __init__(self, nums: List[int]):
#         self.seg_tree = SegmentTree(nums)
#     def sumRange(self, i: int, j: int) -> int:
#         if not self.seg_tree: return 0
#         return self.seg_tree.rFind(self.seg_tree.root, (i, j))

# class SegmentTree:
    
#     def __init__(self, nums):
#         self.count = 0
#         self.buildTree(nums)
        
#     def buildTree(self, nums):
#         if not nums: return None
#         self.root = self.rBuildTree(nums, 0, len(nums) - 1)
        
#     def rBuildTree(self, nums, left, right):
#         if right == left: return Node(nums[left], (left, right))
#         mid = (right + left) // 2
#         new_node = Node(0, (left, right), self.rBuildTree(nums, left, mid), self.rBuildTree(nums, mid + 1, right))
#         new_node.val = new_node.left.val + new_node.right.val
#         return new_node
    
#     def rFind(self, current_node, current_range):
#         if current_range[0] <= current_node.idx_range[0] and current_node.idx_range[1] <= current_range[1]:
#             return current_node.val 
#         elif current_node.idx_range[1] < current_range[0] or current_node.idx_range[0] > current_range[1]:
#             return 0
#         return self.rFind(current_node.left, current_range) + self.rFind(current_node.right, current_range)
            
# class Node:
#     def __init__(self, val, idx_range, left=None, right=None):
#         self.val = val
#         self.idx_range = idx_range
#         self.left = left
#         self.right = right