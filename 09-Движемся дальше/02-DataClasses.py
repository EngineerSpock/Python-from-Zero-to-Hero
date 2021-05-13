#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Question:
    
    def __init__(text, is_true, explanation):
        self.text = text
        self.is_true = is_true
        self.explanation = explanation


# In[ ]:


from dataclasses import dataclass

@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str


# In[ ]:


q = Question("test", True, "because")
q.text


# In[ ]:


q = Question("test", True) # have to init all the attrs


# In[ ]:


@dataclass
class Question:
    text: str = ""
    is_true: bool = False
    explanation: str = ""


# In[ ]:


q = Question()
q.text = "hi"
q.text


# In[ ]:


@dataclass(frozen=True)
class Question:
    text: str
    is_true: bool
    explanation: str
        
q = Question("test", True, "because")
q.text


# In[ ]:


q.text = "change"


# In[ ]:




