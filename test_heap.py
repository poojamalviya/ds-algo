class Heap():
    def __init__(self):
        self.arr = []
        self.size = 0

    def insert(self, ele):
        self.arr.append(ele)
        self.size = self.size +1
        self.prolocate_up(self.size-1)

    def left_child(self, i):
        return i*2 +1

    def right_child(self, i):
        return i*2+2
    
    def parent(self, i):
        return i//2
    
    def prolocate_down(self, i):
        small = i 
        print (i, ) 
        if self.size > self.left_child(i) and self.arr[i] > self.arr[self.left_child(i)]:
            small= self.left_child(i)
        
        if self.size > self.right_child(i) and self.arr[i] > self.arr[self.right_child(i)]:
            small = self.right_child(i)
        
        if i != small:
            self.arr[small], self.arr[i] = self.arr[i], self.arr[small]
            self.prolocate_down(i)
    
    def prolocate_up(self, i):
        while self.parent(i)>= 0 and self.arr[i] < self.arr[self.parent(i)]:
            temp = self.arr[self.parent(i)]
            self.arr[self.parent(i)] = self.arr[i]
            self.arr[i] = temp
            i = self.parent(i)
    
    def remove(self):
        self.arr[0] , self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]
        self.arr.pop()
        self.size = self.size -1
        self.prolocate_down(0)

    def heapsort(self):
        print (self.size, "size")
        for i in range(self.size-1, 0, -1):
            self.prolocate_down(i)
        for i in range(self.size-1, 0, -1):
            self.arr[0], self.arr[i]= self.arr[i], self.arr[0]
            self.prolocate_down(i)



    
    def display(self):
        print(self.arr)


myheap = Heap() 
myheap.insert(4)
myheap.insert(9)
myheap.insert(6)
myheap.insert(5)
myheap.insert(2)
myheap.insert(3) #[4,9,6,5,2,3]
myheap.display()
myheap.remove()
myheap.display()
myheap.heapsort()
        



