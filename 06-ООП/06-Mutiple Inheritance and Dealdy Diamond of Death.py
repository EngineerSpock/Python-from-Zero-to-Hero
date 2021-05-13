#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#no problems with multiple inheritance when there are no shared methods or attributes

class Animal:
    def die(self):
        print('bye-bye')
        self.health = 0
    
class Carnivour:
    def hunt(self):
        print('eating')
        self.satiety = 100
    
class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')


# In[ ]:


# everything is expectable
dog = Dog()
dog.bark()
dog.hunt()
dog.die()


# In[ ]:


class Animal:
    def set_health(self, health):
        print('set in animal')
    
class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')
        
class Mammal(Animal):
    def set_health(self, health):
        print('set in mammal')
    
    
class Dog(Mammal, Carnivour):
    pass


# In[ ]:


dog = Dog()
dog.set_health(10)

Dog.__mro__


# In[ ]:


# What if Dog defines set_health as well and wants to call the base class?

class Animal:
    def set_health(self, health):
        print('set in animal')
    
class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')
        
class Mammal(Animal):
    def set_health(self, health):
        print('set in mammal')
    
    
class Dog(Mammal, Carnivour):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self, health)
        Animal.set_health(self, health)
        
        print('set in dog')


# In[ ]:


dog = Dog()
dog.set_health(10)


# In[ ]:


# any class in a such hierarchy may want to call the base class
# so what to do if each class from the hierarchy calls a method from the base class?

class Animal:
    def set_health(self, health):
        print('set in animal')
    
class Carnivour(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print('set in carnivour')
        
class Mammal(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print('set in mammal')
    
    
class Dog(Mammal, Carnivour):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self, health)
        
        print('set in dog')


# In[ ]:


dog = Dog()
dog.set_health(100)


# Everything seems logical. However, if we create an instance of the base class and the shared method being called, we don't want to initialize the deepest parent twice because of potential bugs.
# 
# Starting with Python 3, we solve this problem using the 'super()' function

# In[ ]:


class Animal:
    def set_health(self, health):
        print('set in animal')
  
        
class Mammal(Animal):
    def set_health(self, health):
        #super().set_health(health)
        print('set in mammal')
        
class Carnivour(Animal):
    def set_health(self, health):
        #super().set_health(health)
        print('set in carnivour')

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        #super().set_health(health)
        
        print('set in dog')    
    
#class Dog(Carnivour, Mammal):
#    def set_health(self, health):
#        super().set_health(health)
        
#        print('set in dog')


# In[ ]:


dog = Dog()
dog.set_health(100)
print(Dog.__mro__)


# Usually, we use this inside __init__()
# What we insvestigated here is called MRO (method resolution order).
# Starting with Python 3 we can use super() being sure in the correct order of calls: from bottom to top and from left to right.
# You can see that the first constructor that finishes its work is the deepest one while the last constructor is the top one. We say "from left to right" because MRO takes the order of inheritance into account. If we change the inheritance order from Mammal, Carnivour to Carnivour, Mammal, we will get another behavior (from left to right).

# In[ ]:


class Dog(Carnivour, Mammal):
    def set_health(self, health):
        super().set_health(health)
        
        print('set in dog')
        
dog = Dog()
dog.set_health(100)


# Long story short, if you need to initialize a base class (and very often we really HAVE TO do that) then to avoid bugs you'd better to use the super() method.

# In[ ]:


class Animal:
    def __init__(self):
        self.health = 100
        
    def hit(self, damage):
        self.health -= damage
            
class Carnivour(Animal):
    def __init__(self):
        #super().__init__()
        self.legs = 4            


# In[ ]:


dog = Carnivour()
dog.hit(10)

print(dog.health)


# In[ ]:


class A: 
    def rk(self): 
        print(" In class A") 
class B(A): 
    def rk(self): 
        print(" In class B") 
class C(A): 
    def rk(self): 
        print("In class C") 

# classes ordering 
class D(B, C): 
    pass

r = D() 
r.rk() 


# In[ ]:


D.__mro__

