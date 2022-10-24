import pygame, sys, random

pygame.init()

negro=(0, 0, 0)
blanco=(255, 255, 255)
verde=(0, 255, 0)
rojo=(255, 0, 0)
azul=(0, 0, 255)

size=(800, 500)

screen=pygame.display.set_mode(size)

reloj=pygame.time.Clock()

lista_coordenadas=[]

for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        lista_coordenadas.append([x, y])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    
    screen.fill(blanco)
    for j in lista_coordenadas:


        x = j[0]
        y = j[1]
        pygame.draw.circle(screen, negro, (x, y), 2)
        j[1] +=1
        if j[1] > 500:
            j[1] = 0

    pygame.display.flip()
    reloj.tick(60)