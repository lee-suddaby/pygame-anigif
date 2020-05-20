import pygame
from anigif import *

pygame.init()
clock = pygame.time.Clock()

height = 360
width = 936

imagesCA = [" "] * 12
for counter in range(12):
    imagesCA[counter] = "frames/coin_frame_" + str(counter+1) + ".png"

coin = AnimatedGif(100,100,96,96,imagesCA) #Two coin animations at the bottom-left and bottom-right corners of the screen

screen = pygame.display.set_mode([250,250])
screen.fill((0,0,0))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    screen.blit(coin.getCurFrame(), [coin.gif_x,coin.gif_y])
    clock.tick(10)
    pygame.display.flip() #Update display

pygame.quit()