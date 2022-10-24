
from operator import truediv
import pygame, sys, random, time

pygame.init()

rosa_pastel=(255, 154, 162)
celeste_pastel=(179, 255, 255)
blanco_pastel=(255, 255, 216)
azul_pastel=(71, 98, 165)
rojo_pastel=(255, 105, 97)
morado_pastel=(204, 169, 221)
naranja_pastel=(255, 117, 20)
negro=(0, 0, 0)
anchura=800
altura=400

#variables de juego
puntaje=0
velocidad=0
jugador_x=50
jugador_y=200
enemigo_x=0
enemigo_y=0
y_cambio=0
gravedad=1
x_cambio=0
obstaculos= [890, 1000, 1500, 2000, 2500]
obstaculo_velocidad = 3
#cambio_obs_velocidad = 1
activo= False


pantalla=pygame.display.set_mode([anchura, altura])
pygame.display.set_caption('Cube Jumper')
fondo= celeste_pastel
fps=60
font = pygame.font.SysFont('8-BIT WONDER', 16)
temporizador=pygame.time.Clock()

funcionar=True

while funcionar:
    temporizador.tick(fps)
    pantalla.fill(fondo)
    if not activo:
        texto_instructivo= font.render(f'Presiona arriba para saltar y derecha e izquierda para moverte', True, blanco_pastel, azul_pastel)
        pantalla.blit(texto_instructivo, (220, 100))


    texto_puntaje= font.render(f'Puntaje: {puntaje}', True, blanco_pastel, azul_pastel)
    pantalla.blit(texto_puntaje, (350, 300))
    piso=pygame.draw.rect(pantalla, rosa_pastel, (0, 220, anchura, 50))
    jugador=pygame.draw.rect(pantalla, blanco_pastel, [jugador_x, jugador_y, 20, 20])
    obstaculo0 = pygame.draw.rect(pantalla, rojo_pastel, [obstaculos[0], 200, 20, 20])
    obstaculo1 = pygame.draw.rect(pantalla, morado_pastel, [obstaculos[1], 200, 20, 20])
    obstaculo2 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[2], 200, 20, 20])
    obstaculo3 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[3], 200, 20, 20])
    obstaculo4 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[4], 200, 20, 20])



    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            funcionar=False
        if event.type==pygame.KEYDOWN and not activo:
            if event.key == pygame.K_UP:
                activo=True
                jugador_x = 50
                puntaje = 0
                obstaculos= [890, 1000, 1500, 2000, 2500]
                obstaculo_velocidad = 3
        if event.type == pygame.KEYDOWN and activo==True:
            if event.key == pygame.K_UP and y_cambio ==0:
                y_cambio= 18
            if event.key == pygame.K_RIGHT:
                x_cambio = 3
            if event.key == pygame.K_LEFT:
                x_cambio = -3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_cambio = 0
            if event.key == pygame.K_LEFT:
                x_cambio = 0  

    for i in range(len(obstaculos)):
        if activo:
            obstaculos[i] -= obstaculo_velocidad
            if obstaculos[i] < -20:
                obstaculos[i] = random.randint(800, 1500)
                puntaje += 1
                if puntaje == 2:
                    obstaculo_velocidad =  1 + obstaculo_velocidad
                    
                if puntaje == 10:
                    obstaculo_velocidad = 2 + obstaculo_velocidad
                
                if puntaje == 20:
                    obstaculo_velocidad = 3 + obstaculo_velocidad
                            
            if jugador.colliderect(obstaculo0) or jugador.colliderect(obstaculo1) or jugador.colliderect(obstaculo2) or jugador.colliderect(obstaculo3) or jugador.colliderect(obstaculo4):
                activo = False 


    if 0 <= jugador_x <= 780:
        jugador_x += x_cambio
    if jugador_x <0:
        jugador_x = 0
    if jugador_x > 780:
        jugador_x = 780

    

    
    

    if y_cambio > 0 or jugador_y < 220:
        jugador_y -= y_cambio
        y_cambio -= gravedad
    if jugador_y > 200:
        jugador_y = 200
    if jugador_y == 200 and y_cambio < 0:
        y_cambio = 0


    pygame.display.flip()
pygame.quit()


