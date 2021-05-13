#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#OOP allows to create their own objects that have methods and attributes
#you already used objects (list and such)
#You can represent the whole world by classes, attributes and methods
#classes can contain data about themselves

#functions are not enough to program large programs (functional programmers are laughing here :))


# In[ ]:


#also keep in mind that sometimes developers use "object" and "class" words interchangeably


# In[ ]:


numbers = [1,2,3] #create/instantiate a built-in list object
type(numbers)


# In[ ]:


class Character():
    pass


# In[ ]:


unit = Character() #create instance
type(unit)


# In[ ]:


# each class has a constructor
# and by the way a class can have more than one constructor
# many objects have attributes that have to be initialized, 
# "name" for a person ; "unique id for a credit card", 
# so constructor is something that makes sure that an object can not be created in an invalid state)


# In[ ]:


class Character():
    
    def __init__(self, race): #self represents an instance
        self.race = race


# In[ ]:


unit = Character() #client creates an instance, and uses 'unit' to work with object while self is used by the class developer


# In[ ]:


unit = Character('Elf')


# In[ ]:


type(unit)


# In[ ]:


unit.race


# In[ ]:


class Character():
    
    def __init__(self, race, damage = 10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


# In[ ]:


unit = Character('Ork', damage=20, armor=40) #though not obliged to write arg names and even pass anything
print(unit.damage)
print(unit.armor)

