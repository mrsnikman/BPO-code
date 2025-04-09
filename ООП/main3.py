'''
Описать классы «Фигура», «4-х угольник», «треугольник», 
«квадрат», «равнобедренный треугольник», «прямоугольный треугольник», «равносторонний треугольник». 
Выстроить правильную иерархию наследования этих классов, определить какие из классов должны быть абстрактными, 
какие методы абстрактными или виртуальными. Описать конструкторы и деструкторы разработанных классов. 
Создать по одному объекту каждого класса, для которого это возможно, поместить их в один массив. 
Для каждого объекта вызвать метод Area (нахождение площади) и вывести на экран все свойства каждого из объектов.
'''

import math
from abc import ABC, abstractmethod


class AbsFigure(ABC):
    @abstractmethod
    def area():
        pass    


class Triangle(AbsFigure):
    def __init__(self, base, height):
        self.base = base
        self.height = height


class Quadrilateral(AbsFigure):
    def __init__(self, length, height):
        self.length = length
        self.height = height
    


class Square(Quadrilateral):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def print_properties(self):
        print(f"Квадрат: side = {self.side}, площадь = {self.area()}")


class IsoscelesTriangle(Triangle):
    def area(self):
        return 0.5 * self.base * self.height
    
    def print_properties(self):
        print(f"Равнобедренный Треугольник: основание = {self.base}, высота = {self.height}, площадь = {self.area()}")


class RightTriangle(Triangle):
    def __init__(self, leg1, leg2):
        self.leg1 = leg1
        self.leg2 = leg2

    def area(self):
        return 0.5 * self.leg1 * self.leg2

    def print_properties(self):
        print(f"Прямоугольный треугольник: катет1 = {self.leg1}, катет2 = {self.leg2}, площадь = {self.area()}")


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, (math.sqrt(3) / 2) * side)

    def area(self):
        return (math.sqrt(3) / 4) * (self.base ** 2)

    def print_properties(self):
        print(f"Равносторонний Треугольник: основание = {self.base}, площадь = {self.area()}")


# Создание объектов
figures = [
    Square(4),
    IsoscelesTriangle(5, 4),
    RightTriangle(3, 4),
    EquilateralTriangle(6)
]

for figure in figures:
    figure.print_properties()

