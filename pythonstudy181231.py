#!/usr/bin/env python
# coding: utf-8

# In[1]:


class A(list):
    def __len__(self):  #重新定义一个len方法
        return 10
a = A()
len(a)


# In[4]:


class B(object):
    def __len__(self):
        return 10
    #def __str__(self):
    #    return 'this is B'
b=B()
print(b)


# In[5]:


from enum import Enum
department = Enum('department',('software','hardware','machine'))
type(department)


# In[6]:


dir(department)


# In[7]:


a = department.software
dir(a)


# In[8]:


#枚举的遍历
#先查看怎么使用资源
mem = department.__members__
dir(mem)


# In[20]:


item = mem.items
dir(item)


# In[28]:


for i,j in item():
    print(i,j.value)


# In[29]:


#自定义枚举类型
from enum import Enum,unique
@unique #用于检测枚举的value唯一
class Department(Enum):
    software = 10
    hartware = 20
    machine = 30


# In[30]:


d = Department
print(d.software.name,d.software.value)

