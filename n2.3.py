def to_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper

@to_string
def add(a, b):
    return a + b


result = add(3, 5)
print(result + " - Это строка")