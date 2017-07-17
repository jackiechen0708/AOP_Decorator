# -*- coding:utf-8 -*-
import time
"""
    如果我们想计算一个函数的运行时间，该咋办？
"""

from BaseFunction import *

"""
    小G：那简单，我们把那个函数开头加一个time记录进入函数的初始时间，最后再加一个time记录退出函数时间，二者相减不就可以了吗
    小K：是可以，但是这样大片大片的Copy代码不符合高端码农的风格哦,而且假如想测另一个函数的时间，还要重新再写第二个对应于此函数的测时间方法，这样代码也是很麻烦的
    小G：也是哦，好尴尬。那该怎么办呢？
    小K：这时就该装饰器模式出场啦，登登等当
"""

def time_fun(fun):
    time1=time.time()
    fun()
    time1=time.time()-time1
    print ("operation time:",time1)

"""
    小K：好了，现在可以用time_fun(fun1)调用来计算fun1运行时间了
    小G：真的诶，好棒啊
"""

time_fun(fun1)




"""
    小K：可是现在函数的调用形式发生了改变，原先调用fun1()的地方现在要改为time_fun(fun1)才能使用
    小G：对的，假如调用的地方很多，那一个个改起来也是蛮麻烦的事情，有没有其它方法可以还是以原形式的方式调用呢
    小K：这个问题问的好，答案是有的,我们加一个内嵌包装函数，包装函数完成计时功能，然后外部函数返回这个内部函数名，这样只要在外部
    加上fun1=time_fun_original(fun1)声明，就可以像原来一样调用函数了
    
"""

def time_fun_original(fun):
    def wrapper():
        time1=time.time()
        fun()
        time1=time.time()-time1
        print ("operation time:",time1)
    return wrapper

fun1=time_fun_original(fun1)

fun1()

"""
然后python有语法糖形式可以简化
fun1=time_fun_original(fun1)
这种写法
"""


fun11()

