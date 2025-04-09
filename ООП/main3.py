'''
Описать классы «Фигура», «4-х угольник», «треугольник», 
«квадрат», «равнобедренный треугольник», «прямоугольный треугольник», «равносторонний треугольник». 
Выстроить правильную иерархию наследования этих классов, определить какие из классов должны быть абстрактными, 
какие методы абстрактными или виртуальными. Описать конструкторы и деструкторы разработанных классов. 
Создать по одному объекту каждого класса, для которого это возможно, поместить их в один массив. 
Для каждого объекта вызвать метод Area (нахождение площади) и вывести на экран все свойства каждого из объектов.
'''

from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrilateral(Figure):
    @abstractmethod
    def diagonal_length(self):
        pass

class Triangle(Figure):
    pass

class Square(Quadrilateral):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def diagonal_length(self):
        return math.sqrt(2) * self.side
    
    def print_properties(self):
        print(f"Квадрат со стороной {self.side} и площадью {self.area()}")

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def print_properties(self):
        print(f"Равнобедренный треугольник с основанием {self.base}, высотой {self.height} и площадью {self.area()}")

class RightTriangle(Triangle):
    def __init__(self, leg_a, leg_b):
        self.leg_a = leg_a
        self.leg_b = leg_b
    
    def area(self):
        return 0.5 * self.leg_a * self.leg_b
    
    def print_properties(self):
        print(f"Прямоугольный треугольник с катетами {self.leg_a} и {self.leg_b} и площадью {self.area()}")

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2
    
    def print_properties(self):
        print(f"Равносторонний треугольник с стороной {self.side} и площадью {self.area()}")
    

# Создание объектов
figures = [
    Square(4),
    IsoscelesTriangle(5, 4),
    RightTriangle(3, 4),
    EquilateralTriangle(6)
]

for figure in figures:
    figure.print_properties()