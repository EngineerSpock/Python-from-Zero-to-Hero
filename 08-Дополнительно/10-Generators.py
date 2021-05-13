#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Напишем функцию, генерирующую случайные числа в установленном диапазоне.


# In[ ]:


import random


# In[ ]:


def randoms(min, max, n):
    return [random.randint(min, max) for _ in range(n)]


# In[ ]:


# сразу же материализует результаты вызова функции randoms
for r in randoms(10, 30, 5):
    print(r)


# In[ ]:


def randoms(min, max, n):
    return yield random.randint(min, max) for _ in range(n)


# In[ ]:


def randoms(min, max, n):
    for i in range(n):        
        yield random.randint(min, max)


# In[ ]:


# казалось бы тоже самое...
for r in randoms(10, 30, 5):
    print(r)


# In[ ]:


# но на самом деле совсем не тоже самое...
rand_sequence = randoms(1, 10, 10)
rand_sequence


# In[ ]:


#if run loop second time, it won't yield anything :)
# they can't be rewound, either run generator again or put in list already generated items
seq = list(randoms(1, 10, 5))
seq


# In[ ]:


# мы можем запросить сгенерировать 10 элементов, а реально материализовать лишь 5

import itertools

rand_sequence = randoms(1, 10, 10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


# In[ ]:


# поскольку генераторы позволяют извне указывать количество элементов на генерацию, то
# зачастую мы делаем бесконечные генераторы, перекладываю ответственность за определение границ на вызывающую сторону

def randoms(min, max):
    while True:
        yield random.randint(min, max)
        
rand_sequence = randoms(1, 10)
five_taken = list(itertools.islice(rand_sequence, 5))
print(five_taken)


# In[ ]:


#if we have a large line-based file, then we can read it lazily to avoid MemoryError


# In[ ]:


def read_line_by_line(file):
    """Lazy function (generator) to read a file line by line."""
    while True:
        line = file.readline()
        if not line:
            break
        yield line


# In[ ]:


file = open(f'C:\\Temp\\test.txt')
for line in read_line_by_line(file):
    print(line.rstrip())


# In[ ]:


rand_sequence2 = randoms(1, 10)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)
n = next(rand_sequence)
print(n)


# In[ ]:


my_list = [1, 2, 3, 4]

# square each term using list comprehension
# Output: [1, 4, 9, 16]
squares = [x**2 for x in my_list]
squares


# In[ ]:


# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
squares = (x**2 for x in my_list)
squares


# In[ ]:


for i in squares:
    print(i)

