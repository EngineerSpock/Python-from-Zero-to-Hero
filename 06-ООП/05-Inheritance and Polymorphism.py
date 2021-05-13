#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Shape():
    
    def __init__(self):
        print('Shape created')
        
    def draw(self):
        print('Drawing a shape')
    
    def area(self):
        print('calc area')
        
    def perimeter(self):
        print('calc perimeter')


# In[ ]:


shape = Shape()


# In[ ]:


class Rectangle(Shape):
    
    def __init__(self, width, height):
        Shape.__init__(self)
        
        self.width = width
        self.height = height
        
        print('Rectangle created')
        
    def draw(self):
        print(f'Drawing rectangle with width={self.width} and height={self.height}')
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)


# In[ ]:


rect = Rectangle()


# In[ ]:


rect = Rectangle(10,15)


# In[ ]:


print(rect.area())


# In[ ]:


print(rect.perimeter())


# In[ ]:


rect.draw()


# In[ ]:


import math
class Triangle(Shape):
    
    def __init__(self, a, b, c):
        Shape.__init__(self)
        
        self.a = a
        self.b = b
        self.c = c
        
        print('Triangle created')
        
    def draw(self):
        print(f'Drawing triangle with sides={self.a},{self.b},{self.c}')
        #Shape.draw(self)
        
    def area(self):
        s = (self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
    
    def perimeter(self):
        return self.a+self.b+self.c


# In[ ]:


triangle = Triangle(10,10,10)


# In[ ]:


triangle.draw()
print(triangle.area())
print(triangle.perimeter())


# In[ ]:


for shape in [rect, triangle]:
    shape.draw()


# In[ ]:


class Shape():
    
    def __init__(self):
        print('Shape created')
        
    def draw(self):
        raise NotImplementedError("Can't instantiate an abstract class")        
    
    def area(self):
        raise NotImplementedError("Can't calc area of an abstract class")
        
    def perimeter(self):
        raise NotImplementedError("Can't calc perimeter of an abstract class")


# In[ ]:


shape = Shape()


# In[ ]:


shape.draw()

