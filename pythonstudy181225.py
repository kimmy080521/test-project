#!/usr/bin/env python
# coding: utf-8

# In[1]:


#递归函数：如果一个函数内部调用了本身，就形成了一个递归函数
#需要防止堆栈溢出
#递归都可以采用循环方式来间接实现功能

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a-1)


# In[2]:


factorial(5)  #计算5的阶乘


# In[4]:


factorial(20)


# In[5]:


factorial(10000)  #RecursionError: maximum recursion depth exceeded in comparison


# In[6]:


#切片。从list，tuple中取数据，可以用索引，循环的方式，也可以用切片
#切片使用方法：[startIndex:endIndex:step]
list1 = list(range(101))
print(list1[10:21])   #前开后闭 10-20


# In[7]:


print(list1[:12])  #不加起始位置，只用截止位置。就是从头取到截止位置


# In[10]:


#复制整个list
list2 = list1[::]
print(list2)


# In[11]:


#取最后10个数
list1[-10:]


# In[12]:


#间隔8个取数据
list1[::8]


# In[13]:


tu1=tuple(list1)


# In[14]:


tu1[2:30:3]


# In[15]:


tu1[-5:]


# In[16]:


#同样的，字符串也可以用切片方式操作
a = 'I love python'


# In[17]:


a[0:10]


# In[18]:


a[:15]


# In[19]:


#可迭代的数据。用for ...in语句 迭代所有可迭代的集合
#可以使用collections模块的Iterable类型
from collections import Iterable
list1=[]
tuple1=()
set1=set()
a='i love python'
b=345
print(isinstance(list1,Iterable))
print(isinstance(tuple1,Iterable))
print(isinstance(set1,Iterable))
print(isinstance(a,Iterable))
print(isinstance(b,Iterable))


# In[20]:


#使用for...in遍历字典
dict1={'name':'kimmy','age':33,'height':175,'weight':72}


# In[22]:


for key in dict1:
    print(key,dict1[key])


# In[23]:


#实现与C一样，带下标的遍历 使用enumerate
list1 = list(range(100))
for i,v in enumerate(list1[:80:7]):
    print(i,v)


# In[24]:


tuple1 = ([1,2,3],[4,5,6],[7,8,9])
for i,j,k in tuple1:
    print(i,j,k)


# In[26]:


#列表生成式，列表生产不再难
list1 = list(range(101))
list2 = [data*2 for data in list1 if data%7==0]
print(list2)


# In[28]:


#双循环
l1 = [1,2]
l2 = [3,4]
l3 = [i*j for i in l1 for j in l2] 
print(l3)


# In[30]:


import os
files = [file for file in os.listdir('.')]  
files


# In[31]:


#生长器generator，节约内存 
list3 = [k*2 for k in range(10)]
list4 = (k*2 for k in range(10))
print(type(list3),type(list4))


# In[32]:


next(list4)


# In[33]:


next(list4)


# In[34]:


next(list4)


# In[36]:


for data in list4:   #遍历，将剩余的显示出来
    print(data)


# In[37]:


next(list4)  #遍历结束后，会报错StopIteration 


# In[39]:


#yeild产生generator
def test():
    print('----------test1-------------')
    yield 1
    print('----------test2-------------')
    yield 2
    print('----------test3-------------')
    yield 3
    print('----------test4-------------')
    return 'ok'


# In[45]:


test1 = test()
print(type(test1))


# In[46]:


while True:
    try:
        print(next(test1))
    except StopIteration as e:
        print(e.value)
        break


# In[57]:


#惰性迭代器Iterator 与Iterable要区别看。list，dict，set，tuple是可迭代的，但不是Iterator
from collections import Iterator   
from collections import Iterable
a=[1,2,3]
b=(3,4,5)
c={6,7,8}
d=set(a)
print(isinstance(a,Iterator))
print(isinstance(b,Iterator))
print(isinstance(c,Iterator))
print(isinstance(d,Iterator))
print(isinstance(a,Iterable))
print(isinstance(b,Iterable))
print(isinstance(c,Iterable))
print(isinstance(d,Iterable))


# In[67]:


#Iterator是惰性的，需要使用next函数才能进行下一次计算
#把Iterable的数据转换成Iterator，需要使用函数iter

aa = iter(a)
bb = iter(b)
print(type(aa),type(bb))


# In[59]:


for data in aa:
    print(data)


# In[60]:


for data in a:
    print(data)


# In[68]:


next(aa)


# In[69]:


#分布式思想map函数,产生的结果是一个Iterator，惰性的。
#接受的参数，第一个是函数，第二个参数是数据流
def fun1(x):
    if((isinstance(x,(int,float)))):
        return x*x
    else:
        print('bad type!')
list1 = list(range(10))
result = map(fun1,list1)
print(type(result),isinstance(result,Iterator))


# In[70]:


list(result)


# In[74]:


#reduce,接受两个参数，一个是函数，一个数数据。实际是一个坐累积的过程。
from functools import reduce
def func2(x,y):
    if(isinstance(x,(int,float)) &isinstance(y,(int,float)) ):
        return x*y
    else:
        print('bad type')
list2 = list(range(1,5))
result2 = reduce(func2,list2)
print(type(result2),result2)


# In[75]:


#filter。和map函数一样，两个参数，一个是函数，一个是Iterable的序列。
#结果是Iterator，惰性的。数据的过滤作用。
def func3(x):
    if(isinstance(x,(int,float))):
        return x % 23 == 0
    else:
        print('bad type')
list3 = list(range(1000))
result3 = filter(func3,list3)
print(type(result3),isinstance(result3,Iterator))
print(list(result3))


# In[79]:


#过滤掉空字符串
def ftnull(s):
    return s and s.strip()
list4 = ['',' I ',' love ',' python ','']
result4 = filter(ftnull,list4)
print(list(result4))


# In[80]:


#sorted 排序函数，可以对list排序
#必选参数Iterable，可选key
list1 = [2,3,4,-55,23,-35,89,12]
sorted(list1,reverse=True,key=abs)


# In[81]:


sorted(list1,reverse=True)


# In[82]:


sorted(list1)


# In[83]:


tuple1=(1,3,67,34,-23,-47)
sorted(tuple1)


# In[85]:


#函数式编程
def  facto(x):
    if(isinstance(x,(int))):
        def f():
            a = 1
            b = 1
            while a<=x:
                b*=a
                a+=1
            return b
        return f
    else:
        print('bad type')


# In[88]:


facto(5)   #结果是一个函数，没有计算结果


# In[89]:


facto(5)()  #计算出实际数值


# In[105]:


def count():
    fs = []
    for i in range(7,10):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count() 
print(f1,f2,f3)       #打印出来的是函数体
print(f1(),f2(),f3()) #打印出来的是结果

g1 = count()
print(g1)     #打印出来的死函数体list
print(g1[0]())   #打印出来的是list的第一个对象


# In[94]:


def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(7,10):
        fs.append(f(i))#f(i)立刻执行
    return fs

f1,f2,f3 = count2()
print(f1(),f2(),f3())


# In[106]:


def count():
    fs = []
    for i in range(7,10):
        def f():
            return i*i
        fs.append(f())     #使用f，返回函数，使用f（）返回计算后的数值
    return fs

f1,f2,f3=count() 
print(f1,f2,f3)       #打印出来的是函数体


# In[ ]:




