import pygame
from pygame.colordict import THECOLORS
import time
pygame.init()
size = ((500,400))
dis = pygame.display.set_mode(size)
font = pygame.font.SysFont('couriernew', 40)
for y in range(-50, size[1] + 50, 1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Фон
    dis.fill(THECOLORS["pink"])
    #Нижний круг
    pygame.draw.circle(dis, (255, 255, 255), (250, 300), 60)
    #Средний круг
    pygame.draw.circle(dis, (255, 255, 255), (250, 200), 45)
    #Верхний круг
    pygame.draw.circle(dis,(255, 255, 255), (250, 120), 35)
    #Шляпа
    hat_color = (0, 0, 0)
    pygame.draw.polygon(dis, hat_color, [
        (220, 95),
        (280, 95),
        (265, 55),
        (235, 55)
    ])
    #Глаза
    pygame.draw.circle(dis, (0, 0, 0), (240, 110), 5)
    pygame.draw.circle(dis, (0, 0, 0), (260, 110), 5)
    #Нос-морковка(треугольник)
    pygame.draw.polygon(dis, (255, 140, 0), [(250, 120), (270, 125), (250, 130)])
    #Пуговицы
    pygame.draw.circle(dis, (0, 0, 0), (250, 180), 5)
    pygame.draw.circle(dis, (0, 0, 0), (250, 200), 5)
    pygame.draw.circle(dis, (0, 0, 0), (250, 220), 5)
    #Руки
    pygame.draw.line(dis, (139, 69, 19), (205, 200), (150, 150), 5)
    pygame.draw.line(dis, (139, 69, 19), (295, 200), (350, 150), 5)
    #Текст
    text = font.render(("HELLO"), True, THECOLORS['white'])
    dis.blit(text, (50, y))

    pygame.display.update()
    # Двигаем текст
    time.sleep(0.01)
quit()