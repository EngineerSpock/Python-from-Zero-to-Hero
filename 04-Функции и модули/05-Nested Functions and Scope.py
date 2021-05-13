#!/usr/bin/env python
# coding: utf-8

# LEGB Rule:
# 
# L: Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.
# 
# E: Enclosing function locals — Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer.
# 
# G: Global (module) — Names assigned at the top-level of a module file, or declared global in a def within the file.
# 
# B: Built-in (Python) — Names preassigned in the built-in names module : open, range, SyntaxError,...

# In[ ]:


greeting = "Hello from the global scope"

def greet():
    #greeting = "Hello from enclosing scope"
    
    def nested():
        #greeting = "Hello from local scope"
        print(greeting)    
    nested()

result = greet()

print(greeting)
result


# In[ ]:


#list = don't override and don't assign


# In[ ]:


greeting = "Hello from the global scope"

def greet(greeting):
    print(f'Greet in func:{greeting}')
    
    greeting = "Hello from enclosing scope"
    
    print(f'Greet in func:{greeting}')
    
    def nested():
        greeting = "Hello from local scope"
        print(greeting)    
    nested()

result = greet("test")

result
print(greeting)


# In[ ]:


greeting = "Hello from the global scope"

def greet():
    global greeting
    print(f'Greet in func:{greeting}')
    
    greeting = "Hello from enclosing scope"
    
    print(f'Greet in func:{greeting}')
    
    def nested():
        greeting = "Hello from local scope"
        print(greeting)    
    nested()

result = greet()

result
print(greeting)

#can't have argument and global for the same name
#avoid using global keyword and use global variables as rarely as possible


# In[ ]:


#if you need to change a value, use a function and return from it new value, don't use globals
#when a global variable is used from different place, then there is a high change of spoiling it unintentionally

