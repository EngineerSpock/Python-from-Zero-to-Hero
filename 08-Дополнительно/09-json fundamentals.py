#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json


# In[ ]:


class Tournament(json.JSONEncoder):
    
    def __init__(self, name, year):
        self.name = name
        self.year = year


# In[ ]:


path = "C:\\Temp\json_test.txt"


# In[ ]:


tournaments = {
    "Aeroflot Open": 2010,
    "FIDE World Cup": 2018,
    "FIDE Grand Prix": 2016
}
json_data = json.dumps(tournaments, indent=2) # serializing
print(json_data)

loaded = json.loads(json_data) # deserializing
print(type(loaded)) 
print(loaded)


# In[ ]:


t1 = Tournament("Aeroflot Open", 2010)
json_data = json.dumps(t1)


# But interestingly, there is the __dict__ on any python object, which is a dictionary used to store an object’s (writable) attributes. We can use that for working with JSON, and that works well.

# In[ ]:


json_data = json.dumps(t1.__dict__)
print(json_data)
t = Tournament(**json.loads(json_data))
print(f'name={t.name}, year={t.year}')


# In[ ]:


# усложним

class ChessPlayer:
    
    def __init__(self, tournaments):
        self.tournaments = tournaments


# In[ ]:


t1 = Tournament("Aeroflot Open", 2010)
t2 = Tournament("FIDE World Cup", 2018)
t3 = Tournament("FIDE Grand Prix", 2016)

p1 = ChessPlayer([t1, t2, t3])


# In[ ]:


json_data = json.dumps(p1.__dict__, indent=4)
print(json_data)


# Alright, it looks like Student is not JSON serializable and our __dict__ trick no longer works. But if we look at the dump function’s documentation, there is a deafult setting that we can use:
# 
#     If specified, default should be a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a TypeError. If not specified, TypeError is raised.
# 
# When serializing, we can use that to serialize the __dict__ property of each object instead of the object itself.

# In[ ]:


json_data = json.dumps(p1, default=lambda o: o.__dict__, indent=4)
print(json_data)


# Basically, all it does is to tell dumps to dump the __dict__ of every object instead of the object itself.

# In[ ]:


decoded_player = ChessPlayer(**json.loads(json_data))
print(decoded_player)


# In[ ]:


st_dict = decoded_player.tournaments[0]
print(type(st_dict))

print(st_dict)


# In[ ]:


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
print(type(json_data))
print(json_data)

decoded_player = ChessPlayer.from_json(json.loads(json_data))
print(decoded_player)
print(decoded_player.tournaments)


# А теперь сериализуем / десерилизуем через файл:

# In[ ]:


with open("player.json", "w") as file:
    json.dump(p1, file, default=lambda o: o.__dict__)
    
with open("player.json", "r") as read_file:
    data = json.load(read_file)
    
print(data)


# In[ ]:


decoded_player = ChessPlayer.from_json(data)
print(decoded_player)
print(decoded_player.tournaments)


# Если есть желание поиграться с json - посетите https://jsonplaceholder.typicode.com
# 
# Можно например выкачать тестовые тудушки, а дальше попарсить их, сгруппировать и т.д.

# In[ ]:


import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos

