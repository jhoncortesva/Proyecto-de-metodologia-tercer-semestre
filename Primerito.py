from ctypes import sizeof
from ssl import VERIFY_DEFAULT
import pygame, sys

pygame.init()

#definir colores

negro=(0, 0, 0)
blanco=(255, 255, 255)
verde=(0, 255, 0)
rojo=(255, 0, 0)
azul=(0, 0, 255)

size=(800, 500)

#crear ventana
screen=pygame.display.set_mode(size)
#controlar fps
reloj=pygame.time.Clock()

#coordenadas
cord_x=400
cord_y=200

#Velocidad a lo que se mueve el dibujo
velo_x=3
velo_y=3

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    #Lógica del juego
    if (cord_x > 720 or cord_x < 0):
        velo_x *= -1
    if (cord_y > 420 or cord_y < 0):
        velo_y *= -1
    cord_x += velo_x
    cord_y += velo_y
    #Lógica del juego
    #poner color de fondo
    screen.fill(blanco)
    #DIBUJAR ACÁ
    # for i in range(100, 700, 100):
        #pygame.draw.rect(screen, negro, (i, 350, 50, 50))

    pygame.draw.rect(screen, negro, (cord_x, cord_y, 80, 80))
    #DIBUJAR EN MEDIO
    #actualizar pantalla
    pygame.display.flip()

    reloj.tick(60)