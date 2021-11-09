def inspect(func):
    def wrapped_function(*args,**kwargs):
        print(f"Running function {func.__name__}")
        val = func(*args,**kwargs)
        print(f"Result is {val}")
        return val
    return wrapped_function

@inspect
def combine (a,b):
    return a+b

class User:
    base_url="https://www.openaapicom"
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    @classmethod
    def query(cls,queryString):
        return cls.base_url + '?' + queryString
    
    @staticmethod
    def name():
        return('Juan')
    
    @property
    def fullname(self):
        return f"{self.firstName} {self.lastName}"