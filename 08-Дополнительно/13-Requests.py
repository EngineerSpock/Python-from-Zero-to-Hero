#!/usr/bin/env python
# coding: utf-8

# https://realpython.com/python-requests/
# https://en.wikipedia.org/wiki/Basic_access_authentication
# https://github.com/encode/httpx
# https://github.com/ross/requests-futures
# 

# In[ ]:


import requests


# In[ ]:


response = requests.get('https://www.engineerspock.com/')


# In[ ]:


response


# In[ ]:


type(response)


# In[ ]:


response.status_code # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes


# In[ ]:


if response: # __bool__() is re-defined - not the same as == 200, many other codes are also considered OK
    print("Works!")


# In[ ]:


from requests import HTTPError
for url in ['https://www.engineerspock.com/', 'https://www.engineerspock.com/inexistent']:
    try:
        response = requests.get(url)
        
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'Error: {http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print('Connected Successfully!')


# In[ ]:


response = requests.get('https://www.engineerspock.com/')
response.content # in bytes

# response.text # in str


# In[ ]:


#charset=utf-8 в теле ответа, но может и не быть и если надо установить явно, то перед взятием text:
response.encoding = 'utf-8'


# In[ ]:


response = requests.get('https://api.github.com')
response.text


# In[ ]:


data = response.json()
data


# You can do a lot with status codes and message bodies. But, if you need more information, like metadata about the response itself, you’ll need to look at the response’s headers.

# In[ ]:


blog_response = requests.get('https://www.engineerspock.com/')
github_response = response = requests.get('https://api.github.com')


# In[ ]:


print(blog_response.headers, end='\n') # look for metadata
print('')
print(github_response.headers, end='\n')


# теперь мы можем опрашивать этот словарь, причём имена ключей не чувствительны к регистру ибо спецификация HTTP это позволяет

# In[ ]:


placeholder_response = requests.get("http://jsonplaceholder.typicode.com/comments", params=b'postId=1')


# In[ ]:


placeholder_response.text


# In[ ]:


placeholder_response.json()


# # POST, PUT, DELETE

# According to the HTTP specification, POST, PUT requests pass their data through the message body rather than through parameters in the query string. 
# 
# data takes a dictionary, a list of tuples, bytes, or a file-like object. 

# In[ ]:


import json

class Tournament(json.JSONEncoder):
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)
        
class ChessPlayer:
    
    def __init__(self, tournaments):
        self.tournaments = tournaments
        
    @classmethod
    def from_json(cls, json_data: dict):
        tournaments = list(map(Tournament.from_json, json_data["tournaments"]))
        return cls(tournaments)
        
t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament("FIDE Grand Prix", 2016)

p1 = ChessPlayer([t1, t2, t3])

json_data = json.dumps(p1, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# In[ ]:


response = requests.post('https://httpbin.org/post', json=json_data)
json_response = response.json()


# In[ ]:


print(json_response['data'])


# In[ ]:


json_response['headers']['Content-Type']


# # Authentication
# 
# ## Basic Auth

# In[ ]:


from getpass import getpass
auth_response = requests.get('https://api.github.com/user', auth=('EngineerSpock', getpass())) 
# no HTTP, only HTTPS!
# requests validate SSL certs automatically though you can turn that off

# also can pass HTTPBasicAuth explicitly, or we can just send a tuple like above


# In[ ]:


auth_response.json()


# # Timeout, Session

# In[ ]:


from requests.exceptions import Timeout
try:
    response = requests.get('https://www.engineerspock.com', timeout=1)
except Timeout:
    print('The request timed out')


# In[ ]:


# each get or post creates new connection to remote server
# often, we prefer to keep connection alive and proceed with once established credentials


# In[ ]:


with requests.Session() as session:
    session.auth = ('EngineerSpock', getpass())

    response = session.get('https://api.github.com/user')
    
print(response.json())


# In[ ]:


from requests.adapters import HTTPAdapter

adapter = HTTPAdapter(max_retries=3)

with requests.Session() as session:
    session.mount('https://api.github.com/', adapter)
    session.auth = ('EngineerSpock', getpass())
    
    try:
        session.get('https://api.github.com/user')
    except ConnectionError as err:        
        print(f'Failed to connect:{err}')
    else:
        print('OK')

