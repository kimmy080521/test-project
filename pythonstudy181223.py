#!/usr/bin/env python
# coding: utf-8

# In[1]:


name = input()
age = input()
print ("hello",name,"you age is :",age)


# In[2]:


type(100)


# In[3]:


type(3.1415)


# In[4]:


type("abc")


# In[7]:


type('abc')


# In[10]:


print('abc\td')
print('abc\nd')
print(r'abc\nd')


# In[12]:


print('''
a
b
c
\td
e\n
f

''')


# In[14]:


True


# In[15]:


False


# In[18]:


type(True)


# In[19]:


print(type(True))


# In[20]:


print(True and False)


# In[21]:


print(True or False)


# In[22]:


print(None)
type(None )


# In[23]:


a = 'I love python'
print(a,type(a))
a = 123
print (a,type(a))


# In[24]:


PI = 3.1415926
print(PI)
PI = 3.14
print(PI)


# In[25]:


print('我爱python')


# In[35]:


ord('爱')


# In[36]:


ord('爱')


# In[37]:


chr(29233)


# In[55]:


print('hello')
print(b'hello')


# In[56]:


name = input()
age = input()
print ("hello %s, your age is %d" %(name,int(age)))


# In[59]:


list1 = list()
list2 = ['c','d']
print(type(list1),type(list2))


# In[60]:


print(len(list1))
print(len(list2))


# In[61]:


list1.append('c')


# In[62]:


print(list1)


# In[64]:


list1.append('cde')


# In[67]:


list1.insert(1,'insert1')


# In[68]:


print(list1)


# In[69]:


list1.append('zh')


# In[70]:


print(list1)


# In[71]:


list1.extend(list2)


# In[72]:


list1


# In[73]:


a = list1.pop()


# In[74]:


a


# In[75]:


b = list1.pop(1)
print(b)


# In[76]:


list1


# In[77]:


list1.remove('zh')


# In[78]:


list1


# In[79]:


list1[0]=[1,2,3,4]


# In[80]:


list1


# In[81]:


list1.append(1)
list1.append(1)
list1.append(1)
list1.append(1)
list1.append(2)


# In[82]:


list1.count(1)


# In[83]:


list1


# In[84]:


list2


# In[85]:


list3=[1,2,3,4,5,6,12,3,4,6,9]


# In[86]:


list3


# In[87]:


list3.sort()


# In[88]:


list3


# In[89]:


list3.reverse()


# In[90]:


list3


# In[91]:


print(list3)
print(list3[-1])
print(list3[3])


# In[ ]:




