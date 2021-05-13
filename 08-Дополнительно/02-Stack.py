#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class MyStack:
    def __init__(self):
        self.array = []
    
    def push(self, item):
        self.array.append(item)
        
    def pop(self):
        popped_item = self.array.pop()
        return popped_item
    
    def peek(self):
        return self.__current()
    
    def count(self):
        return len(self.array)
    
    def __iter__(self):
        self.index = self.count() - 1
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration 
        result = self.array[self.index]
        self.index -= 1
        return result
    
    def __current(self):
        return self.array[self.count()-1]


# In[ ]:


stack = MyStack()


# In[ ]:


stack.push(1)
stack.push(2)
stack.push(3)


# In[ ]:


stack.pop()


# In[ ]:


stack.peek()


# In[ ]:


stack.count()


# In[ ]:


stack.push(4)
stack.push(5)
stack.push(6)


# In[ ]:


for i in stack:
    print(i)

