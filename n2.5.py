def replace_result(replacement_value):
    def decorator(func):
        def one(*args, **kwargs):
            result = func(*args, **kwargs)
            return replacement_value
        return one
    return decorator
@replace_result("Оформите подписку Premium+ для того чтобы узнать ответ!")
def summa(a, b):
    return a + b

print('Проффесианальный складыватель чисел')
result = summa(int(input('1 число: ')), int(input('2 число: ')))
print(result)