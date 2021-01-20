class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head

        while current is not None:
            print(current.data)
            current =  current.next
    
    def insert_at_tail(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next
        temp.next = Node(data)

    def insert_at_head(self, data):
        newNode = Node(data)
        if self.head is not None:
            newNode.next = self.head
        
        self.head = newNode

    def insert_at_position(self, data, n):
        temp = self.head
        counter = 0
        while temp is not None:
            temp= temp.next

            if (counter== n-1):
                nextadd= temp.next
                newNode= Node(data)
                newNode.next= nextadd
                temp.next = Node(data)
            counter = counter +1


    # 1 => 2  => 3


list1 = LinkedList()
list1.insert_at_head(1)
list1.insert_at_head(2)
list1.insert_at_head(3)


list2 = LinkedList()
list2.insert_at_tail(4)
list2.insert_at_tail(5)
list2.insert_at_tail(6)
list2.insert_at_tail(7)
list2.insert_at_tail(8)

list2.insert_at_position(9, 3)
# list1.head = Node(1)

# ele2 = Node(2)
# ele3 = Node(3)

# list1.head.next =  ele2
# ele2.next = ele3

list1.printList()
list2.printList()










# def insert_at_head(self, data):
#     newNode = Node(data)
#     if self.head != None:
#         newNode.next = self.head
#     self.head = newNode

# def insert_at_tail(self, data):
#     if self.head is None:
#         self.head = Node(data)
#         return 
#     temp = self.head
#     while temp.next is not None:
#         temp = temp.next
#     temp.next = Node(data)
