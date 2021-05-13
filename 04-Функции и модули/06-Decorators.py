#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def hello_world():
    print('Hello, world!')
hello_world()


# In[ ]:


hello2 = hello_world
hello2()


# In[ ]:


#return func from func
#pass in a func as an arg


# In[ ]:


def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished its work')
    return wrap


# In[ ]:


def hello():
    print('hello, world!')


# In[ ]:


wrapped_by_logger = log_decorator(hello)
wrapped_by_logger()


# In[ ]:


@log_decorator
def hello():
    print('hello, world!')


# In[ ]:


hello()


# In[ ]:


#decorators are used by frameworks extensively, that's why it's important to understand what they are in essence


# In[ ]:


from timeit import default_timer as timer
import math
import time

def measure_exectime(func):
    def inner(*args, **kwargs):
        start = timer()
        
        func(*args, **kwargs)
        
        end = timer()
        
        print(f'Function {func.__name__} took {end-start} for execution')
    return inner

@measure_exectime
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))


# In[ ]:


factorial(100)

