def fun1():
    print ("hello1")


def decorate(func):
    print ("hellon2")
    # func()
    print (func.__name__)

# decorate(fun1)

