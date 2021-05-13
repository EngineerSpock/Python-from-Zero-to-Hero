def log_decorator(func):
    def wrap():
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished its work')
    return wrap

@log_decorator
def hello():
    print('hello, world!')
    
hello()

help(hello)

from functools import wraps
def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func {func}')
        func()
        print(f'Func {func} finished its work')
    return wrap
    
@log_decorator
def hello():
    print('hello, world!')
    
help(hello)