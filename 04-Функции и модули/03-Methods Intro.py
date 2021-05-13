#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#why we need functions? - clean code, reusable code, separation of responsibilities (even of programmers)

#describe the signature
def greeting():
    print('Hello!')
    
#greeting
#greeting()

#help(greeting) -?

'''
DOCSTRING: Information about the function
INPUT: no input...
OUTPUT: Hello ...
'''


# In[ ]:


#def print_name(name):
def print_name(name='Default'):
    print(name)
    
print_name('Elijah')
#print_name() #no args if there's a default value


# In[ ]:


result = print_name()
print(result)
print(type(result))


# In[ ]:


def get_greeting(name):
    return 'Hello ' + name

greeting = get_greeting('Elijah')


# In[ ]:


def get_sum(a, b):
    return a + b

result = get_sum(10, 2)
result


# In[ ]:


def is_adult(age):
    return age > 18

is_adult = is_adult(20)
is_adult


# In[ ]:


def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome('aabaa'))
print(is_palindrome('aabba'))


# In[ ]:


def calc_taxes(p1, p2, p3):
    return sum((p1, p2, p3)) * 0.06


# In[ ]:


calc_taxes(10, 20, 30)
#calc_taxes(10, 20, 30, 40) - error


# In[ ]:


def calc_taxes(*args):
    for x in args:
        print(f'Got payment = {x}')
    return sum(args) * 0.06


# In[ ]:


print(calc_taxes(10, 20, 30))
print(calc_taxes(10, 20, 30, 40))


# In[ ]:


def save_players(**kwargs):
    for k, v in kwargs.items():
        print(f'Player {k} has rating {v}')
        
save_players(Carlsen=2800, Giri=2780)


# In[ ]:


#args and kwargs can be mixed in a signature

