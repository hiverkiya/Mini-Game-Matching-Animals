import pygame
from pygame import display,event,image

pygame.init() # Initializes all imports which we will be using

display.set_caption('Animals Matching')
screen=display.set_mode((512,512))# Return screen as surface object
matched=image.load('other_assets/matched.png') # also returns surface element
screen.blit(matched,(0,0)) #blit method displays surface on surface
display.flip()
running= True

while running:
    current_events=event.get()
    for e in current_events:
        if e.type == pygame.QUIT: #Generated when we close the window
            running=False

print(' Goodbye !')            
