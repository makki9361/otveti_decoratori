class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height


a = Rectangle(int(input("Введите ширину: ")), int(input("Введите высоту: ")))
print("Площадь прямоугольника:", a.area)