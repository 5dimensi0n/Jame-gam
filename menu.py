
import pygame
from jamejam import *
import math

pygame.init()
font = pygame.font.SysFont("Consolas", 30)

window = pygame.display.set_mode((600, 600))
play = pygame.Rect(425, 200, 140, 50)
quit = pygame.Rect(425, 400, 140, 50)

playtext = font.render("Play", True, (252, 251, 252))
quittext = font.render("Quit", True, (252, 251, 252))

pygame.display.set_caption('Meow')
run = True
while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(mouse):
                game()
            if quit.collidepoint(mouse):
                run = False
    
    mouse = pygame.mouse.get_pos() 
    window.fill((45,39,50))
    t = pygame.time.get_ticks() / 2 % -750
    window.blit(pygame.transform.scale((pygame.image.load('sprites/player.png')), (600,(math.sin(t/240.0) * 20 + 600))), (0,-math.sin(t/240.0) * 25 - 20))

    pygame.draw.rect(window, (0,156,137), play)
    pygame.draw.rect(window, (0,156,137), quit)

    window.blit(playtext, (450, 200))
    window.blit(quittext, (450, 400))
    pygame.display.flip()   
pygame.quit()
