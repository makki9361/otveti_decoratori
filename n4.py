import math
class Circle:
    @staticmethod
    def area(radius):
        return math.pi * radius ** 2


radius = int(input("Введите радиус: "))
print("Площадь круга равна: ", Circle.area(radius))