'''
Создать класс Payment (зарплата). 
В классе должны быть представлены поля: фамилия-имя-отчество, оклад, год поступления на работу, процент надбавки, подоходный налог, 
количество отработанных дней в месяце, количество рабочих дней в месяце, начисленная и удержанная сумма. 
Реализовать методы: вычисления начисленной суммы, вычисления удержанной суммы, вычисления суммы, выдававаемой на руки, вычисления стажа. 
Стаж вычисляется как полное количество лет, прошедших от года поступления на работу, до текущего года. Начисления представляют собой сумму, начисленную за отработанные дни, и надбавки. 
Удержания представляют собой отчисления в пенсионный фонд (1% от начисленной суммы) и подоходный налог (13%).

fio = фамилия-имя-отчество
salary = оклад
year of employment = год поступления на работу
percentage of bonus = процент надбавки
income tax = подоходный налог (13%)
current days worked = количество отработанных дней в месяце
working days in month = количество рабочих дней в месяце
accrued amount = начисленная суммма
withheld amount = удержанная сумма
experience = стаж
'''

import math
from abc import ABC, abstractmethod

class Payment():
    def __init__(self, fio="Иванов Иван Иванович", salary=0, year_of_employment=2025, percentage_of_bonus=0.0):
        self.fio = fio
        self.salary = salary
        self.year_of_employment = year_of_employment
        self.percentage_of_bonus = percentage_of_bonus
        self._income_tax = 0.13
        self._current_days_worked = 0
        self.working_days_in_month = 30
        self._accrued_amount = 0
        self._withheld_amount = 0
        print(f"Зарплата сотрудника {fio} успешно создана.")
    
    
    def calculate_accrued_amount(self):
        '''
        Метод для вычисления начисленной суммы
        '''
        self._accrued_amount = self.salary/self.working_days_in_month*self._current_days_worked*(1+self.percentage_of_bonus)
        return(self._accrued_amount)
        

    def calculate_withheld_amount(self):
        '''
        Метод для вычисления удержанной суммы
        '''
        self._withheld_amount = self._accrued_amount*(0.01+self._income_tax)
        return self._withheld_amount

    def calculate_payment_amount(self):
        '''
        Метод для вычисления сумма, выдававаемой на руки
        '''
        payment_amount = self._accrued_amount-self._withheld_amount
        print(f"Cумма, выдававаемая на руки: {payment_amount}")

    def calculate_experience(self, current_year):
        '''
        Метод для вычисления стажа
        '''
        if(current_year>=self.year_of_employment):
            experience = current_year-self.year_of_employment
            print(f"Cтаж: {experience}")
        else:
            print("Сотрудник из будущего")
        

    def add_days_worked(self, days=1):
        '''
        Метод для добавления рабочих дней
        '''
        if(self.working_days_in_month>=days):
            if(self._current_days_worked+days<=self.working_days_in_month):
                self._current_days_worked+=days
                print(f"Добавлено рабочих дней {days}.")
            else:
                print(f"Внимание! Текущее число дней превышает количество дней в месяце")
                print(f"Рабочие дни не добавлены")
        else:
            print(f"Внимание! Указанное число дней превышает количество дней в месяце")
            print(f"Рабочие дни не добавлены")

    def __del__(self):
        print(f"Зарплата сотрудника {self.fio} успешно удалена.")



#Основной код программы    
name = str(input("Введите ФИО сотрудника: "))
salary = float(input("Введите оклад сотрудника: "))
year = int(input("Введите год принятия на работу: "))
bonus = float(input("Введите оклад сотрудника(0.02): "))
employee1 = Payment(name, salary, year, bonus)

days = int(input("Введите число отработанных рабочих дней в месяце: "))
employee1.add_days_worked(days)
print()
print("Расчёт сумм")
print(f"начисленная сумма: {employee1.calculate_accrued_amount()}")
print(f"Удержанная сумма: {employee1.calculate_withheld_amount()}")
print()

days = int(input("Введите число отработанных рабочих дней, которое необходимо добавить: "))
employee1.add_days_worked(days)
print()
print("Расчёт сумм")
print(f"начисленная сумма: {employee1.calculate_accrued_amount()}")
print(f"Удержанная сумма: {employee1.calculate_withheld_amount()}")
print()

employee1.calculate_payment_amount()
employee1.calculate_experience(2025)
