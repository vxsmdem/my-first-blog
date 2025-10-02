import pygame

pygame.init()
size = ((500,400))
dis = pygame.display.set_mode(size)
dis_over = False
while not dis_over:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
             pygame.quit()
     for i in range(13):
        for j in range(13):
            pygame.draw.rect(dis, (130, 150, 70), (50 * i, 50 * j, 40, 40))


     pygame.display.update()
quit()
