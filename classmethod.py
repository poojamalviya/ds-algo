class Person:
    def __init__(self, name, age):
        self.name = name
        self.age =  age

    # @classmethod
    def display(self):
        print (self.name +" is:" + str(self.age))

p = Person('Pooja', 25)
# p.display()

def my_decorator(myfunc):
    print("hellooo1")
    myfunc()
    print('hello2')


@my_decorator
def tryFunction():
    print("thisssss")
