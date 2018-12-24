#!/usr/bin/env python
# coding: utf-8

# In[1]:


tuple1 = tuple()
tuple2 = ()
print(type(tuple1),type(tuple2))


# In[2]:


tuple1 =(1) #如果不加逗号，将会被认为是int型
print(type(tuple1))


# In[3]:


tuple1 = (1,)
print(type(tuple1))


# In[5]:


list2 = [1,2,3,4]
tuple2 = (list2,'a','b','c')


# In[6]:


tuple2


# In[7]:


list2.append(5)


# In[8]:


tuple2    #虽然tuple不可以改变，但是包含的list类型可以被修改。


# In[12]:


a = []   #True list()
if a:
    print('a is True')
else:
    print('a is False')


# In[15]:


name = input()
age = int(input())
if age>18:
    print('hello %s,your age is %d' % (name,age))
else :
    print('hello %s,you age is so small' %(name))


# In[16]:


name = input()
age = int(input())
if age>18:
    print('hello %s,your age is %d' % (name,age))
else :
    print('hello %s,you age is so small' %(name))


# In[18]:


list1 = [1,2,3,4,5,'a','b']
for data in list1:
    print(data)


# In[19]:


tuple1=(1,2,3,4,5,'a','s')
for data in tuple1:
    print(data)


# In[27]:


a = range(101)
sum1 = 0
for i in a:
    sum1+=i
print('1 to 100 sum is: %d' %(sum1))


# In[29]:


list1 = range(100)
list2 = [data*2 for data in list1 if data%3 == 0]
print(list2)  #通过for，重新组成一个新的list


# In[31]:


sum2 = 0
a =0
while a <=100:
    sum2+=a
    a+=1
print('1 to 100 sum is %d' %(sum2))


# In[32]:


dict1 = dict()
dict2 ={}
print(type(dict1),type(dict2))


# In[33]:


dict1['kimmy']=[88,89,87]  #向字典里增加信息
dict1['allen']=[88,85,83]
dict1


# In[34]:


dict1['allen']=[99,93,94] #替换掉之前的信息，只能有一个allen
dict1


# In[36]:


dict1.pop('allen') #删除allen


# In[37]:


dict1


# In[38]:


dict1['kimmy']=[ 99,98,97]  #修改内容，就直接把内容重新输入一遍


# In[39]:


dict1


# In[40]:


'allen' in dict1 #查找是否存在key值


# In[41]:


'kimmy' in dict1


# In[44]:


if 'allen' in dict1:
    pass
else :
    print('allen is not in dict1')


# In[45]:


print(dict1.get('allen'))  #通过get方法查找某个元素


# In[46]:


print(dict1.get('kimmy'))


# In[47]:


set1 = set([1,2,3,3,3,4,5,5])
set1


# In[48]:


set1.add('abc')


# In[49]:


set1


# In[50]:


set1.remove(3)


# In[51]:


set1


# In[52]:


set2 = set([3,4,6,'abc','det'])


# In[53]:


print('交集：',set1&set2)


# In[54]:


print('并集：',set1|set2)


# In[55]:


list1 = [1,2,3,4,5,6,7,8]
print('max is : %d' %(max(list1)))


# In[56]:


print('min is : %d' %(min(list1)))
print('sum is : %d' %(sum(list1)))


# In[57]:


list2 = list1
list2.append('a')


# In[58]:


print('max is : %d' %(max(list1)))  #max传入的参数错误，会报typeerror


# In[59]:


help(sum)


# In[60]:





# In[62]:


#定义函数
#def 函数名（参数列表：）
#代码块
#return 返回值
def fun1(a,b):
    return a+b
fun1(4,6)


# In[63]:


#解决函数参数传递错误问题
fun1(2,'s') #会报错，typeerror


# In[70]:


def fun1(a,b):
    if(isinstance(a,(int,float)) & isinstance(b,(int,float))):
        return a+b
    else:
        print('bad type')

fun1(4,6)


# In[71]:


fun1(4,'a')


# In[74]:


def sum2(a,b):
    if(isinstance(a,(int,float)) & isinstance(b,(int,float))):
        return a+b,a-b,a*b
    else:
        print('bad type')


# In[75]:


result = sum2(6,3)
print('result is')


# In[78]:


def sum3(a,b,c=10): #位置参数
    if(isinstance(a,(int,float)) & isinstance(b,(int,float))):
        return a+b+c,a-b-c,a*b*c
    else:
        print('bad type')


# In[79]:


sum3(40,30)


# In[82]:


#可变参数
def sum4(*args):
    a=0
    for i in args:
        a+=i
    return(a)


# In[83]:


sum4(1,2,3,4,5,6)


# In[84]:


list1 = list(range(100))
print(sum4(*list1)) #将list传递给函数，就在前面加*


# In[85]:


#关键字参数，**kv实际是一个字典结构
def student(name,age,**kv):
    print(name,age,kv)
    print(type(kv))


# In[86]:


student('kimmy',33,height = 175,weight=70)


# In[89]:


#命名关键字参数
def student1(name,age,*,height,weight):
    print(name,age,height,weight)


# In[90]:


student1('kimmy',33,height=185,weight=80)


# In[96]:


#参数列表里如果有了*args，可以省略单独的*
def student2(name,age,*args,height,weight):
    print(name,age,*args,height,weight)


# In[97]:


student2('allen',33,'student','man',height = 175,weight = 76)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




