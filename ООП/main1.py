'''
Создать класс Point для работы с точками на плоскости, координаты точки – декартовы. 
Обязательно должны быть реализованы: перемещение точки по оси Х, перемещение по оси Y, 
определение расстояния до начала координат, расстояние между двумя точками.
'''

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def move_x(self, move_x):
        pass

    @abstractmethod
    def move_y(self, move_y):
        pass

    @abstractmethod
    def distance_to_zero(self):
        pass

    @abstractmethod
    def distance_to(self, other):
        pass

class Point(Shape):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f"Точка с координатами ({x}, {y}) успешно создана.")
    
    def move_x(self, move_x):
        '''
        Метод для передвижения объекта по оси x 
        '''
        self.x += move_x


    def move_y(self, move_y):
        '''
        Метод для передвижения объекта по оси y
        '''
        self.y += move_y


    def distance_to_zero(self):
        '''
        Метод для определения растояния до нулевой координаты (0, 0)
        '''
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        '''
        Метод для определения расстояния между двумя точками
        '''
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def print_coords(self, name):
        '''
        Метод для вывода координат в консоль
        '''
        print(f"Координаты {name}: ({self.x}, {self.y})")
    
    def __del__(self):
        print(f"Точка с координатами ({self.x}, {self.y}) успешно удалена.")

#Основной код программы    
x1 = float(input("Введите координату x для точки p1: "))
y1 = float(input("Введите координату y для точки p1: "))
p1 = Point(x1, y1)

x2 = float(input("Введите координату x для точки p2: "))
y2 = float(input("Введите координату y для точки p2: "))
p2 = Point(x2, y2)

p1.print_coords("p1")
p2.print_coords("p2")

move_x = float(input("Введите величину перемещения по оси X для p1: "))
move_y = float(input("Введите величину перемещения по оси Y для p1: "))
p1.move_x(move_x)
p1.move_y(move_y)
print(f"После перемещения p1: ({p1.x}, {p1.y})")

distance_to_zero = p1.distance_to_zero()
print(f"Расстояние p1 до начала координат: {distance_to_zero}")

distance = p1.distance_to(p2)
print(f"Расстояние между p1 и p2: {distance}")