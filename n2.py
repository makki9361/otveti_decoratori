class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32


a = Temperature(36)
print("В Цельсиях:", a.celsius)
print("В Фаренгейтах:", a.fahrenheit)