
import pygame
import jamejam

pygame.init()
font = pygame.font.SysFont("Consolas", 30)

window = pygame.display.set_mode((600, 600))
play = pygame.Rect(250, 200, 140, 50)
quit = pygame.Rect(250, 400, 140, 50)

playtext = font.render("Play", True, (255,255,255))
quittext = font.render("Quit", True, (255,255,255))

pygame.display.set_caption('Meow')
run = True
while run:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play.collidepoint(mouse):
                jamejam.game()

            if quit.collidepoint(mouse):
                run = False
    
    mouse = pygame.mouse.get_pos() 
    window.fill((0,0,0))
    

    pygame.draw.rect(window, (255,0,255), play)
    pygame.draw.rect(window, (255,0,255), quit)

    window.blit(playtext, (250, 200))
    window.blit(quittext, (250, 400))
    pygame.display.flip()   
pygame.quit()
