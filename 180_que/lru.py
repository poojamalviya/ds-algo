class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = None(0,0)
        self.tail = None(0,0)
        self.head.prev = self.tail
        self.tail.next = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        