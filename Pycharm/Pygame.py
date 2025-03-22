import pygame
pygame.init() 


surface = pygame.display.set_mode((1920,1800))
pygame.display.set_caption("Resizable")

running  = True

while running:  

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
           running = False

    color = (255, 0, 0)

    if pygame.key. == True:    
        surface.fill(color)


pygamew.display.flip()