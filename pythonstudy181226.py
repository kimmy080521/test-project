#!/usr/bin/env python
# coding: utf-8

# In[2]:


#匿名函数，只有函数体，没有函数名
#lambda表达式是最常用的匿名函数。
#只能有一个表达式，不能有return语句
list1 = list(range(1,11))
result1 = map(lambda x:x*x ,list1)
list(result1)


# In[4]:


fun1 = lambda x:x*x
fun1(9)


# In[ ]:


#装饰器Decorator,可以增强函数功能。相当于给你函数加个外套


# In[5]:


print(fun1,__name__)


# In[41]:


def wrapper(func):
    def f(*args,**kv):
        print("log > args:%s,kv:%s"%(args,kv))
        return func(*args,**kv)
@wrapper
def hehe():
    print('i love python')


# In[12]:


hehe()


# In[19]:


@wrapper
def hehehe(**kv): #加两个星号，输入的参赛是dict类型的
    print('i love python,too')
hehehe(name = 'kimmy')


# In[20]:


@wrapper
def hehehehe(*args):# 加一个星号，输入的参数是tuple类型的
    print('i love python,too')
hehehehe(23,45)


# In[22]:


@wrapper
def hehehehe(*args,**kv):# 加一个星号，输入的参数是tuple类型的,#加两个星号，输入的参赛是dict类型的
    print('i love python,too')
hehehehe(23,45,67,name = 'kimmy')


# In[39]:


def wrapper(text):
    def f1(func):
        def f(*args,**kv):
            print("log > %s,%s"%(text,func.__name__))
            return func(*args,**kv)
        #f.__name__=func.__name__
        return f
    return f1
@wrapper('start to run')
def hehe(**kv):
    print('i love python')
hehe(name = 'kimmy')
print(hehe.__name__)


# In[26]:


import functools
def wrapper(text):
    def f1(func):
        @functools.wraps(func) #可以起到类似作用#f.__name__=func.__name__
        def f(*args,**kv):
            print("log > %s,%s"%(text,func.__name__))
            return func(*args,**kv)
        #f.__name__=func.__name__
        return f
    return f1
@wrapper('start to run')
def hehe(**kv):
    print('i love python')
hehe(name = 'kimmy')
print(hehe.__name__)


# In[42]:


#偏函数 partial
print(int('10',base = 2))


# In[44]:


import functools
f = functools.partial(int,base=8)
f('12')


# In[3]:


#面向对象编程
#数据封装，继承，多态
#class  Animal(object)

class Animal(object):
    pass
dog = Animal()
print(type(dog))


# In[2]:


dog.age = 2
print(dog.age)


# In[12]:


class Animal(object):
    def __init__(self,age):  #类中第一个变量永远是self
        self.__age = age
    def getInfo(self):
        print('self info:age = %d'%(self.__age))
        
dog = Animal(8)


# In[13]:


dog.getInfo() #传参数的时候，不需要传self，python默认代劳


# In[14]:


dog1 = Animal(2)


# In[15]:


print(dog1 == dog) #对比两个类的地址，为false，说明是不同的地址


# In[32]:


#访问限制
class Student(object):
    def __init__(self,name,age):
        self.__name = name   #__name是内部变量，不能直接访问
        self.__age = age
    def getName(self):
        return self.__name   #需要用函数的方式返回内部变量的值
    def setName(self,name):
        self.__name = name
student = Student('kimmy',33)
print(student.getName())
student.setName('allen')
print(student.getName())
student.__name = 'Jimmy'   #这样并不能修改私有变量的值
student._Student__name = 'Jimmy'  #这样才能修改私有变量
print(student.getName())
student


# In[28]:


class Student(object):
    def __init__(self,name,age,weight,height):
        self.__name = name   
        self.__age = age
        self.__weight__=weight  
        self._height = height
student = Student('kimmy',33,70,175)
student.__weight__   # 如果前后都加上__,可以直接访问
student._height  #只加一个_,可以直接访问，但是不建议这么操作


# In[26]:


student._Student__name  #实际上带__的私有变量可以通过这种方式直接访问

