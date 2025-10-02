# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.voice = "Мяу"
#
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.voice = "Гав"
#
# cat = Cat("Мурка")
# dog = Dog("Шарик")
#
# print(f"{cat.name} говорит:", cat.voice)
# print(f"{dog.name} говорит:", dog.voice)
from itertools import count
from tkinter.dnd import dnd_start

from django.db.models.expressions import result


# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def divade(self, a, b):
#         return a / b
#     def multiply(self, a, b):
#         return a * b
# calc = Calculator()
# print(calc.add(10, 5))
# print(calc.subtract(10, 5))
# print(calc.multiply(10, 5))
# print(calc.divade(10, 5))

# class Rectangle:
#     def __init__(self, a, b):
#         self.width = a
#         self.length = b
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
# rect1 = Rectangle(40, 40)
# print("rect1 площадь:", rect1.area())
# print("rect1 периметр:", rect1.perimeter())
#
# rect2 = Rectangle(20, 30)
# print("rect2 площадь:", rect2.area())
# print("rect2 периметр:", rect2.perimeter())

# class BankAccount:
#     def __init__(self, number, sum):
#         self.account_number = number
#         self.balance = sum
#         print(f"Создан счет Начальный баланс: {sum} единиц")
#     def add(self, sum):
#         self.balance = self.balance + sum
#         print(f"На счет зачислено: {sum} единиц")
#     def withdraw(self, sum):
#         if self.balance >= sum:
#             self.balance = self.balance - sum
#             print(f"Со счета снято: {sum} единиц")
#         else:
#             print("Недостаточно средств на счете")
#
# acc1 = BankAccount("123456577", 1000)
# acc1.add(200)
# acc1.withdraw(500)
# acc1.withdraw(300)
# acc1.withdraw(900)

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def print_persons(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
# tom = Person("Tom", 39)
# tom.__name = "Человек паук"
# tom.__age = -129
# tom.print_persons()

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#     def set_age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print("Недопустимый возраст")
#     def get_age(self):
#         return self.__age
#     def get_name(self):
#         return self.__name
#     def print_person(self):
#         print(f"Имя: {self.__name}\tВозраст: {self.__age}")
#
# tom = Person("Tom", 39)
# tom.print_person()
# tom.set_age(-3486)
# tom.set_age(25)
# tom.print_person()