import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
screen=pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()
WHITE=(255,255,255)
running=True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.flip()
pygame.quit()

