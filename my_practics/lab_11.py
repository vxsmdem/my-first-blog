# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.voice = "Мяу"
#
# class Dog:
#     def __init__(self, name):
#          self.name = name
#          self.voice = "Гав"
#
# cat = Cat("Мурка")
# dog = Dog("Шарик")
#
# print(f"{cat.name} говорит:", cat.voice)
# print(f"{dog.name} говорит:", dog.voice)
from os import write

# import message
# print(message.hello)
# message.print_message("Hello work")

# myfile = open("hello.txt", "w")
# import os
# from fileinput import filename
#
#
# def get_world(filename):
#     with open(filename, encoding="utf8") as file:
#         text = file.read()
#     text = text.replace("\n", " ")
#     text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
#     text = text.lower()
#     words = text.split()
#     words.sort()
#     return words
#
# def get_words_dict(words):
#     words_dict = dict()
#
#     for word in words:
#         if word in words_dict:
#             words_dict[word] = words_dict[word] + 1
#         else:
#             words_dict[word] = 1
#     return words_dict
#
# def main():
#     filename = input("Введите путь к файлу: ")
#     if not os.path.exists(filename):
#         print("Указанный файл не существует")
#     else:
#         words = get_world(filename)
#         words_dict = get_words_dict(words)
#         print(f"Кол-во слов: {len(words)}")
#         print(f"Кол-во уникальных слов: {len(words_dict)}")
#         print("Все использованные слова:")
#         for word in words_dict:
#             print(word.ljust(20), words_dict[word])
#
# if __name__ == "__main__":
#         main()
with open("number.txt", "w") as file:
import random
for i in range(100):
    print(random.randrange(0, 101))
file.close()