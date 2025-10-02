# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.voice = "Мяу"
#
# class Dog:
#      def __init__(self, name):
#         self.name = name
#         self.voice = "Гав"
#
# cat = Cat("Мурка")
# dog = Dog("Шарик")
#
# print(f"{cat.name} говорит:", cat.voice)
# print(f"{dog.name} говорит:", dog.voice)

import pygame
pygame.init()
dis=pygame.display.set_mode((500,400))
dis_over=False
while not dis_over:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
              print(event)
              pygame.quit()
     house = pygame.Rect(150, 175, 200, 200)
     color = (150, 70, 70)
     pygame.draw.rect(dis, color, house, 0)
     door = pygame.Rect(225, 275, 50, 100)
     color = (80, 50, 125)
     pygame.draw.rect(dis, color, door, 0)
     window = pygame.Rect(275, 200, 50, 50)
     color = (100, 80, 70)
     pygame.draw.rect(dis, color, window, 0)
     color = (139, 69, 19)
     pygame.draw.line(dis, color,[150, 175], [250, 75], width=5)
     pygame.draw.line(dis, color, [250, 75], [350, 175], width=5)

     pygame.display.update()
quit()

