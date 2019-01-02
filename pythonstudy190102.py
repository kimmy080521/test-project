#!/usr/bin/env python
# coding: utf-8

# In[2]:


#元类
#使用type方法创建class，需要传入三个参数
#1、class名称
#2、基类集合
#3、class方法与函数的绑定字典
def f(self):
    print('i can run')
Student = type('Student',(object,),dict(run=f))
student = Student()
student.run()   #输出i can run


# In[ ]:


#metaclass元类，用于创建类
#创建metaclass一般以Metaclass结尾，需要传入四个参数
#1、当前准备创建的类  2、类的名字  3、类基础的基类集合、4


# In[6]:


class CMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['speak'] =  lambda self,attr : print(attr)
        return type.__new__(cls,name,bases,attrs)
class N(metaclass = CMetaclass):
    pass


# In[7]:


n = N()


# In[8]:


n.speak('i can speak')


# In[9]:


#python里的错误处理
#错误：1、程序编写错误，有bug、2.用户输入错误。
#异常：1、网络异常，磁盘写满。这些异常必须处理，不然会异常退出
#调试：debug，打印日志
#测试：编写完成以后，需要进行测试


# In[11]:


#状态码来表示程序运行情况。404页面不存在，502服务器异常
#try except finally
def f(args):
    try:
        print('start')
        a=10/args
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('end...')
f(10)


# In[12]:


f(0)


# In[15]:


#BaseException包含了所有的异常，会首先报错
def f(args):
    try:
        print('start')
        a=10/args
    except BaseException as e:
        print('BaseException')
        print(e)
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
        print(e)
    finally:
        print('end...')
f(0)


# In[17]:


def f(args):
    try:
        print('start')
        a=10/args
        print('test')  #发生错误以后，不会运行这句
    except ZeroDivisionError as e:
        print('ZeroDivisionError')
        print(e)
    finally:
        print('end...')


# In[18]:


f(0)


# In[30]:


#logging的用法
import logging
def f(args):
    try:
        logging.info('start')
        a=10/args
        logging.info('test')  #发生错误以后，不会运行这句
    except ZeroDivisionError as e:
        logging.info('ZeroDivisionError')
        logging.error(e)
    finally:
        logging.info('end...')
f(0)


# In[31]:


#自定义错误类
class MyError(BaseException):
    pass
def f(args):
    raise MyError('this is my error')
f(1)


# In[ ]:





# In[ ]:





# In[ ]:




