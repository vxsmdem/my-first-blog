# num = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{num} * {i} = {num * i}")
# num = int(input("Введите число: "))
# s = 0
# print("S =", end=" ")
# for i in range(1, num + 1):
#     s += i
#     if i < num:
#         print(i, end=" + ")
#     else:
#         print(i, end=" ")
# print(" =", s)
# secret = 7
# print('Я загадала число от 1 до 10. Поробуй угадать!')
# while True:
#     num = int(input("Введите число: "))
#     if num > secret:
#         print('Загаданное число меньше')
#     elif num < secret:
#         print('Загаданное число больше')
#     else:
#         print('Поздровляю! Ты угадал число:', secret)
#         break
# num = int(input("Введите число:"))
# print(num,"=", num // 60, "часа",num % 60, "минут")
# string = "hello world"
# for char in string:
#     print(char)
# string = "hello world"
# sub_string1 = string[:5]
# print(sub_string1)  # hello
# sub_string2 = string[2:5]
# print(sub_string2)  # llo
# sub_string3 = string[2:9:2]
# print(sub_string3)  # lowr
# from os.path import split
#
# text = "Сегодня десятое сентября"
# words = text.split()
# length = len(split(text))
# print(words, "В этом предложении пробелов:", length)
# while True:
#     num1, num2 = int(input("Введите первое число: ")), int(input("Введите второе число: "))
#     print("Сумма чисел:", num1 + num2)
#     str = input("Нажмите Y или y для завершения программы: ")
#     if (str =="Y" or str =="y"):  break
# string = input("Введите число: ")
# if string.isnumeric():
#     number = int(string)
#     print(number)