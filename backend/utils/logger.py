import time 
from flask import request

def timeis(func): 
    '''Decorator that reports the execution time.'''
  
    def wrap(*args, **kwargs): 
        auth_header = request.headers.get('Authorization')
        if auth_header is not None:
            print('Auth token found')
        else:
            print('No Authorization header found')
        start = time.time() 
        result = func(*args, **kwargs) 
        end = time.time() 
          
        print(func.__name__, end-start) 
        return result 
    return wrap 