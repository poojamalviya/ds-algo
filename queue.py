class Queue():
    def __init__(self):
        self.arr= []
        self.size= 0

    def enqueue(self, ele):
        self.arr.append(ele)
        self.size = self.size+1

    def dequeue(self):
        if self.size >0:
            for i in range(0, self.size-1, 1):
                self.arr[i]= self.arr[i+1]
            self.arr.pop()
            self.size= self.size-1
            
    def get_front(self):
        temp = self.arr[0]
        self.dequeue()
        return temp



my_queue= Queue()
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.get_front()
print my_queue.arr
print my_queue.size
my_queue.dequeue()
print my_queue.arr
print my_queue.size
my_queue.get_front()
