def message_decorator(func):
    def one(*args, **kwargs):
        print("ОаОА... А")
        return func(*args, **kwargs)
    return one
@message_decorator
def vazhnaya_funcia(world):
    return f"hello, {world}!"


print(vazhnaya_funcia("world"))