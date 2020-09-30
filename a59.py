import pygame

pygame.init()

Display=pygame.display.set_mode((400,400))
pygame.display.set_caption('First')

clock=pygame.time.Clock()

pygame.Circle(Display,(0,0,0),(200,200))

crashed=False

while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True


    Display.fill((125,125,225))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

    
