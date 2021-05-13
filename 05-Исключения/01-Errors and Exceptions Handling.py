#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ошибки в любом случае случаются
#баги 
#ошибки из-за неправильного использования объектов
#->необходима обработка ошибок
#без обработки ошибок скрипт сразу останавливается


# In[ ]:


def divide(a, b):
    try:
        return a / b

divide(4, 2)


# In[ ]:


divide(4, 0)


# In[ ]:


divider = input()
divide(4, divider)


# In[ ]:


file = None
try:
    open(r'C:\tmp\abracadabra.txt')
    data = file.read()
except FileNotFoundError as ex:
    print(f'Error has occured. Description:{ex.strerror}')
else:
    print('maybe else')
finally:
    if file:
        file.close()
        
print('doing some work here')


# In[ ]:


def get_int():
    while True:
        try:
            reply = int(input('Enter a number...'))
        except:
            print('Not a number! Try again.')
            continue            
            
get_int()

