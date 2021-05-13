#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from abc import ABC, abstractmethod


# In[ ]:


class Shape(ABC):
    
    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def draw(self):
        pass
        # print('Drawing a shape')
    
    @abstractmethod
    def area(self):
        pass
        # print('calc area')
        
    @abstractmethod
    def perimeter(self):
        pass
        # print('calc perimeter')
        
    def drag(self):
        print('Basic dragging functionality')


# In[ ]:


s = Shape()


# In[ ]:


class Triangle(Shape):
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def draw(self):
        print(f'Drawing triangle with sides={self.a},{self.b},{self.c}')
        
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c
    
    def drag(self):
        super().drag()
        print('Additional actions')


# In[ ]:


t = Triangle(10, 10, 10)


# In[ ]:


t.perimeter()


# In[ ]:


t.drag()

