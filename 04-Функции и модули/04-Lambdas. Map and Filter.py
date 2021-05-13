#!/usr/bin/env python
# coding: utf-8

# Let's look at possible ways of transformation one sequence of values to another.

# In[ ]:


def square(*args):
    return [x*x for x in args]


# In[ ]:


result = square(1,2,3,4,5)
result


# In[ ]:


def triple(*args):
    return [x*3 for x in args]


# In[ ]:


result = triple(1,2,3,4,5)
result


# The number of possible transformations is limitless, so it's impossible to expose so many functions that they will cover all the cases.
# This is one of the reasons why functions can take other functions as arguments and why lambdas exist. But first things first.

# In[ ]:


def square(number):
    return number*number

numbers = [1,2,3,4,5]
#here I should expand help and show that map takes another func as arg
map(square, numbers)


# map() returns an iterable object, so if we do not assign the result of calling map, we will see just the memory location of the resulting object. Another important fact here is that we pass a function's name into map() without specifying the parenthesis. This is because we pass a reference to the function, we do not call it. Using the reference we passed in, the map function will call it on its own when needed. Such a necessity will arise when someone asks for the resulting object to yield the outcome values. Let's iterate through the resulting object to see this. 

# In[ ]:


for x in map(square, numbers):
    print(x)
    
#if we call map(square(), numbers) - it won't work


# In[ ]:


list(map(square, numbers))


# map() transforms one sequence of elements to another sequence applying some transformating function to each element.
# Another common task is to filter the sequence excluding a part of elements by some condition. For that, we have another function called "filter" (what a surprise!)

# In[ ]:


def is_adult(age):
    return age >= 18

ages = [14, 18, 21, 16, 30]


# In[ ]:


filter(is_adult, ages)


# Notice that filter() expects a function which returns boolean. Calling that function and passing in the elements, it will get booleans in return and all the cases that result in false will be filtered out. 

# In[ ]:


list(filter(is_adult, ages))


# And now we approach the notion of a lambda expression (also known as "anonymous functions").
# The thing is that it's too costly to define separate functions only for passing them in map or filter functions.
# If such a function is not going to be used anywhere else, then it means it is not going to be reused and such a function is going to produce more noise rather then a signal. That's exactly when lambdas come into play.

# How to transform this into a labmda?
# def is_adult(age):
#    return age >= 18

# In[ ]:


is_adult = lambda age: age >= 18 #can't have more than one statement in lambda


# In[ ]:


list(filter(is_adult, ages))


# In[ ]:


lambda age: 
    print(f'{age}')
    return age >= 18


# In[ ]:


list(filter(lambda age: age >= 18, ages))


# In[ ]:


multiplier = lambda x, y: x * y
multiplier(2, 3)

