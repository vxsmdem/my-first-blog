# n = input('Введите предложения: ')
# a = 0
# b = 0
# for symbol in n:
#     if symbol == " ":
#         a += 1
#     if symbol.isalpha():
#         b += 1
# print("Пробелов:", a)
# print("Букв:", b)
# string = "hello world"
# sub_string1 = string[:5]
# print(sub_string1)
# sub_string2 = string[2:5]
# print(sub_string2)
# sub_string3 = string[2:9:2]
# print(sub_string3)
# def sum(a,b):
#     return a + b
# result = sum(4, 6)
# print(f"sum(4, 6) = {result}")
# print(f"sum(3, 5) = {sum(3, 5)}")
# def print_person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name} Age: {age}")
# print_person("Tom", 22)
# print_person("Bob", -102)
# def say_hello(): print("Hello")
# def say_hello(): print("Good Bye")
# message = say_hello
# message()
# message = say_goodbye
# message()
# def sum(a, b): return a + b
# def multiply(a, b): return a * b
# operation = sum
# result = operation(5, 6)
# print(result)
# operation = multiply
# print(operation(5, 6))
# def do_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")
# def sum(a, b): return a + b
# def multiply(a, b): return a * b
# do_operation(5, 4, sum)
# do_operation(5, 4, multiply)
# s = input("Ввудите предложения: ")
# a = 0
# b = 0
# while s:
#     if s[0] == " ":
#         a += 1
#     if s[0].isalpha():
#         b += 1
#     s = s[1:]
# print("Пробелов:", a)
# print("Букв:", b)

# num = input('Введите число: ')
# total = 0
# expression = ""
# a = 0
# while a < len(num):
#     digit = int(num[a])
#     total += digit
#     expression += num[a]
#     if a < len(num) - 1:
#         expression += "+"
#     a += 1
# print(expression, "=", total)
# num = int(input("Ввудите число: "))
# total = 0
# parts = ""
# while num > 0:
#     digit = num % 10
#     total += digit
#     parts = str(digit) + (+)