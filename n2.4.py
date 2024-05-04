def catch_exception(func):
    def one(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as a:
            print(f"Исключение: {a}")
    return one
@catch_exception
def exc(a, b):
    return a / b


exc(10, 0)
exc(10, "fsgterge")
exc(10, 0,1)

