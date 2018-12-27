#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Animal(object):
    def fly(self):
        print('i can fly')


# In[2]:


class Dog(Animal): #继承Animal，就可以把Animal的fly方法继承过来
    pass


# In[3]:


class Cat(Animal):
    pass


# In[5]:


dog = Dog()
cat = Cat()
print(type(dog),type(cat))


# In[6]:


dog.fly()
cat.fly()


# In[7]:


#dog 和 cat 不会飞，需要重新定义fly方法，这样就形成了多态
class Dog(Animal): 
    def fly(self):  #重新定义，实现多态
        print('i am a dog,  i can not fly')   
dog = Dog()
dog.fly()


# In[8]:


class Cat(Animal):
    def fly(self):
        print('i am a cat, i can not fly')
cat = Cat()
cat.fly()


# In[9]:


print(isinstance(cat,Animal))  #cat 属于Animal，True


# In[10]:


print(isinstance(cat,Cat))   #True
print(isinstance(cat,Dog))   #False


# In[14]:


#多态的好处，我们传入的只要是基类类型，程序就会自动调用基类或子类
def run(animal):
    if(isinstance(animal,Animal)):
        animal.fly()
    else:
        print('bad type')
        animal.fly()   #为了测试bird类而添加
run(dog)


# In[12]:


#静态语言和动态语言
#静态语言有严格的类型判断，动态语言没有。
#一个对象“看起来像鸭子，走起路来像鸭子”，就可以被看成鸭子


# In[15]:


class Bird(object):
    def fly(self):
        print('i am a bird, i can fly')
bird = Bird()
run(bird)  #虽然bird不属于Animal类，但是它有fly方法，因此也可以执行


# In[16]:


type(dog)
type(cat)


# In[17]:


print(isinstance(dog,Dog))


# In[18]:


print(isinstance(dog,Cat))


# In[19]:


#查看一个实例有哪些方法，可以使用dir
dir(dog)


# In[21]:


import os
dir(os)


# In[22]:


hasattr(dog,'age') #判断是否有某个属性


# In[23]:


getattr(dog,'age') #AttributeError: 'Dog' object has no attribute 'age'


# In[24]:


setattr(dog,'name','xiaohei')


# In[25]:


getattr(dog,'name')


# In[26]:


getattr(dog,'weight','30')#如果没有某个属性，可以直接赋值，然后get


# In[27]:


fly=getattr(dog,'fly')


# In[28]:


type(fly) #method


# In[29]:


fly()  #i am a dog,  i can not fly


# In[32]:


#the attribute ofclass & the attribute of living example
class Student(object):
    pass


# In[33]:


student = Student()
student.name = 'kimmy'
student.age = 33       #在实例中绑定了新的属性


# In[37]:


student1 = Student() #重新定义的实例，不包含之前在实例中增加的属性


# In[39]:


class Student(object):  #在类中增肌的属性，实例中自然继承
    name = 'kimmy'
    age = 33
    pass
student1 = Student()
print(student1.name)


# In[41]:


student1.name = 'allen'    # 实例中可以修改类中属性的值
print(student1.name     #实例的优先级高于类的优先级


# In[47]:


#为了防止胡乱增加属性，可以使用__slots__来限制增加属性
#但是不影响子类的属性添加，也就四说，子类可以随便添加属性
class Student(object):
    __slots__=('name','age')
stu = Student()
stu.name = 'kimmy'
stu.age = 33
print('name is %s,age is %d'%(stu.name,stu.age))


# In[48]:


stu.weight = 72    #AttributeError: 'Student' object has no attribute 'weight'


# In[49]:


class SubStudent(Student):
    pass
stu2 = SubStudent()
stu2.weight = 70


# In[50]:


print(stu2.weight)#重新定义一个子类，可以添加其他的属性


# In[53]:


#property 装饰器的使用，可以很方便的实现get和set功能
class Student(object):
    @property
    def name(self):
        print('get was called')
        return self.__name
    @name.setter
    def name(self,name):
        print('setter was celled')
        self.__name=name

        
s = Student()
s.name = 'kimmy'  #s.set.name
s.name    #s.get.name


# In[55]:


#多重继承，可以继承多个类。
class Flyable(object):
    def fly(self):
        print('i can fly')
class Runable(object):
    def run(self):
        print('i can run')
class Animal(Flyable,Runable):
    pass
animal = Animal()
animal.fly()
animal.run()


# In[57]:


#但是在实际工作中，建议大家多用组合，少用继承
class Animal():
    flyable = Flyable()
    runable = Runable()
animal = Animal()
animal.flyable.fly()
animal.runable.run()


# In[ ]:





# In[ ]:





# In[ ]:




