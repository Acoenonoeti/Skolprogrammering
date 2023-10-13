import pygame
import time
pygame.init()
screen = pygame.display.set_mode([400,300])
pygame.display.set_caption("FUNGERA BARA")
x = 200
y = 150
done = False
clock = pygame.time.Clock()
while not done:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            done = True
        elif pygame.key.get_pressed():
            x -= 1
    pygame.draw.circle(screen, [255,0,255],[x,y],20,2,draw_bottom_right=True)
    pygame.display.flip()
    clock.tick(20)
pygame.quit()