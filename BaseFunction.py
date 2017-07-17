from time import sleep
import time
# from TestDecorator import time_fun_original

def time_fun_original(fun):
    def wrapper():
        time1=time.time()
        fun()
        time1=time.time()-time1
        print ("operation time:",time1)
    return wrapper
def fun1():
    sleep(1)
    print ("Hello World")

@time_fun_original
def fun11():
    sleep(1)
    print ("Hello World")

def fun2(name):
    sleep(2)
    print ("Hello World"+name)


def fun3(name):
    sleep(3)
    return name+"hi"


