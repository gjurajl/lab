import pygame

pygame.init()

pygame.display.set_caption("Lab2")
WIDTH = 800
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,0,0))
pygame.display.update()

#WALLS
wcolor = pygame.Color("purple")
BORDER = 20
#top wall
# Rect((left, top), (width, height)) -> Rect
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(WIDTH,BORDER)) )
#left wall
pygame.draw.rect(screen, wcolor, pygame.Rect((0,0),(BORDER,HEIGHT)) )
#bottom wall
pygame.draw.rect(screen, wcolor, pygame.Rect((20,460),(780,20)) )
# pygame.draw.rect(screen, wcolor, pygame.Rect(?) )

pygame.display.update()


# define a variable to control the main loop
running = True
    
# main loop
while running:
    # event handling, gets all event from the event queue
    for event in pygame.event.get():
        # only do something if the event is of type QUIT
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            running = False