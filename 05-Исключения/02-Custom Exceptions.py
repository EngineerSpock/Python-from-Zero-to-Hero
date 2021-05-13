#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

def calc_square(ab, ac, bc):
    p = (ab + ac+ bc) /2
    s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))
    
    return s


# In[ ]:


square = calc_square(10, 10, 10)
print(square)


# In[ ]:


square = calc_square(-2, 8, 8)
print(square)


# In[ ]:


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise ValueError
        
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))
    
    return s


# In[ ]:


square = calc_square(-2, 8, 8)
print(square)


# In[ ]:


class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""


# In[ ]:


def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangleError('One of the sides is less or equal to 0.')
        
    p = (ab + ac + bc) / 2
    s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))
    
    return s


# In[ ]:


try:
    square = calc_square(10, 10, 10)
    print(square)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(f'We are in else {square}')


# In[ ]:


try:
    square = calc_square(-2, 10, 10)
    print(square)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(f'We are in else {square}')

