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
rosa_pastel=(255, 209, 220)
celeste_pastel=(81, 209, 246)
fuente_pequeña=pygame.font.SysFont('monospace', 25)





reloj=pygame.time.Clock()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        
        screen.fill(celeste_pastel)
        pygame.draw.rect(screen, rosa_pastel, (240, 50, 300, 400))
        etiqueta= fuente_pequeña.render("Cube Jumper", 1, (negro))
        screen.blit(etiqueta, (315, 130))

       
    
    

    pygame.display.flip()
    reloj.tick(60)
