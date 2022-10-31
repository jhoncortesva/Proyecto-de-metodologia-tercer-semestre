from turtle import width
import pygame, sys, random

pygame.init()
size=(800, 500)
screen=pygame.display.set_mode(size)

negro=(0, 0, 0)

blanco=(255, 255, 255)
verde=(0, 255, 0)
rojo=(255, 0, 0)
azul=(0, 0, 255)
rosa_pastel=(250, 128, 114)
celeste_pastel=(0, 128, 128)
azul=(176, 224, 230)
fuente_pequeña=pygame.font.SysFont('monospace', 25)
negrita1 = pygame.font.SysFont("Algerian", 30)
negrita = pygame.font.SysFont("Algerian", 28)

reloj=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        
        screen.fill(celeste_pastel)
        pygame.draw.rect(screen, negro, pygame.Rect(242, 52, 300, 400), border_radius=17)
        pygame.draw.rect(screen, rosa_pastel,(240, 50, 300, 400), border_radius=17)
        
        etiqueta= negrita1.render("CUBE JUMPER", 1, (negro))
        screen.blit(etiqueta, (305, 130))
        etiqueta2= negrita1.render("V 1.0", 1, (negro))
        screen.blit(etiqueta2, (360, 170))
        pygame.draw.rect(screen, azul, (330, 310, 125, 75), border_radius=17)
        etiqueta3= negrita.render("PLAY", 1, (negro))
        screen.blit(etiqueta3, (355, 335))
        

       
    
    

    pygame.display.flip()
    reloj.tick(60)
