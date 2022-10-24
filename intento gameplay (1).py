from operator import truediv
from pygame import mixer
import pygame, sys, random, time

mixer.init()

pygame.init()
#rosas
rosa_pastel=(255, 154, 162)
rosa_pastel_oscurito=(204, 143, 148)
rosa_pastel_oscuro=(201, 153, 175)
rosa_pastel_bajo=(222, 110, 106)
#rosas
celeste_pastel=(179, 255, 255)
blanco_pastel=(255, 255, 216)
verde=(43, 153, 53)
azul_pastel=(71, 98, 165)
rojo_pastel=(255, 105, 97)
morado_pastel=(204, 169, 221)
naranja_pastel=(255, 117, 20)
atardecer=(253, 223, 126)
verde_oscuro=(45, 87, 44)
verde2=(189, 174, 110)
negro=(0, 0, 0)
anchura=800
altura=400
color_piso=rosa_pastel

frases_feas=["Prueba abrir los ojos", "Una vuelta mas a la manzana", "Hoy podría ser el día", "Son solo 4 botones", "¡Tú Puedes!", "¡Excelente Trabajo!", "Vamos, una vez mas", "¿Nota superior?", "¡Lo intentamos!", "...Jhon estuvo aquí..."]
frase_escoger=random.choice(frases_feas)

lista_coordenadas=[]

for i in range(60):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        lista_coordenadas.append([x, y])


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
activo= False
salud=500
mixer.set_num_channels(20)


pantalla=pygame.display.set_mode([anchura, altura])
pygame.display.set_caption('Cube Jumper')
fondo= celeste_pastel

fondo2= atardecer
fps=60
font = pygame.font.SysFont('8-BIT WONDER', 16)
temporizador=pygame.time.Clock()

funcionar=True


while funcionar:
    
    temporizador.tick(fps)
    pantalla.fill(fondo)
    if not activo:
        
        texto_instructivo= font.render(f'Para empezar ¡Salta!', True, azul_pastel)
        pantalla.blit(texto_instructivo, (350, 100))
        texto_instructivo2= font.render(f'Utiliza las flechas para moverte y saltar', True, azul_pastel)
        pantalla.blit(texto_instructivo2, (300, 130))
        texto_aleatorio= font.render(f'Algo para empezar: {frase_escoger}', True, naranja_pastel)
        pantalla.blit(texto_aleatorio, (350, 350))
        texto_credito= font.render(f'Créditos por la música: J-J-Jump Main Theme - Dave Cowen', True, naranja_pastel)
        pantalla.blit(texto_credito, (10, 330))

    texto_puntaje= font.render(f'Puntaje: {puntaje}', True, rojo_pastel)
    pantalla.blit(texto_puntaje, (350, 300))
    texto_salud= font.render(f'SALUD: {salud} HP', True, rojo_pastel)
    pantalla.blit(texto_salud, (350, 340))
    piso=pygame.draw.rect(pantalla, color_piso, (0, 220, anchura, 50))
    jugador=pygame.draw.rect(pantalla, verde, [jugador_x, jugador_y, 20, 20])
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
                mixer.music.load('Skyarenastageidle.wav')
                mixer.music.play(-1)

                activo=True
                salud=500
                jugador_x = 50
                puntaje = 0
                obstaculos= [890, 1000, 1500, 2000, 2500]
                obstaculo_velocidad = 3
                fondo = celeste_pastel
                color_piso=rosa_pastel
        if event.type == pygame.KEYDOWN and activo==True:
            if event.key == pygame.K_UP and y_cambio ==0:
                y_cambio= 18
                saltar=mixer.Sound('efectosalto.wav')
                saltar.play()
            if event.key == pygame.K_RIGHT:
                x_cambio = 2
            if event.key == pygame.K_LEFT:
                x_cambio = -2
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
            if puntaje == 10:
                color_piso=rosa_pastel_bajo
                obstaculo_velocidad = 4
                fondo= fondo2

            if puntaje > 54:
                for j in lista_coordenadas:
                    

                    x = j[0]
                    y = j[1]
                    pygame.draw.circle(pantalla, blanco_pastel, (x, y), 2)
                    j[1] +=1
                    if j[1] > 500:
                        j[1] = 0
            if puntaje == 30:
                obstaculo_velocidad = 5
                fondo = verde2
                color_piso=rosa_pastel_oscurito
            if puntaje == 55:
                obstaculo_velocidad = 8
                color_piso=rosa_pastel_oscuro
                mixer.music.load('skyarenafinal.wav')
                mixer.music.play(-1)
                fondo= negro

                
                
                

            if jugador.colliderect(obstaculo0) or jugador.colliderect(obstaculo1) or jugador.colliderect(obstaculo2) or jugador.colliderect(obstaculo3) or jugador.colliderect(obstaculo4) :
                
                salud= salud-1
                

            if salud == 0:
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

#Música cortesía de Multiversus - Warner Bros Games

