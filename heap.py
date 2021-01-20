class Heap():  #minheap
    def __init__(self):
        self.arr = []
        self.size= 0

    def insert(self, ele):
        print self.size
        if self.size == 0:
            self.arr.append(ele)
            self.size = self.size+1
        else:
            self.arr.append(ele)
            self.size = self.size+1
            print self.size, " / / / / / / "
            self.percolateeup(self.size)

    def remove(self):
        self.arr[0] , self.arr[self.size-1]= self.arr[self.size-1], self.arr[0]
        self.size = self.size-1
        self.percolatedown(0)
    
    def get_parent(self, i):
        return i//2
    
    def get_left_chile(self, i):
        return i*2 +1
    
    def get_right_child(self, i):
        return i*2+2


    def percolateeup(self, i):
        print i, '- - '
        while i//2 >0:
            parent_index = self.get_parent(i)
            print parent_index, i, "???", self.arr
            print self.arr[parent_index], ">>>", self.arr[i] 
            if self.arr[parent_index]< self.arr[i]:
                temp = self.arr[parent_index]
                self.arr[parent_index] = self.arr[i]
                self.arr[i]= temp
    
    def percolatedown(self, i):
        while (i < self.size):
        
            largest = i
            left_child =self.get_left_chile(i)
            right_child = self.get_right_child(i)

            if self.arr[left_child] > self.arr[largest] : 
                largest = left_child
            if self.arr[right_child]> self.arr[largest] :
                largest = right_child
            if (i != largest):
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                self.percolatedown(i)

    def display(self):
        print (self.arr)


# arr= [12, 34, 45, 23, 22, 6 ,5]
myheap = Heap()

myheap.insert(12)
# myheap.insert(2)
myheap.insert(34)
myheap.insert(45)
myheap.insert(23)
# myheap.insert(22)
# myheap.insert(6)
# myheap.insert(5)
# myheap.insert(23)
myheap.display()


        


        


