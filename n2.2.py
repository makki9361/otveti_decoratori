def doubler(func):
    def one(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return one
@doubler
def vazhnaya_funcia(world):
    print(f"hello, {world}!")

vazhnaya_funcia('world')