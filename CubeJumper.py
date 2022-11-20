from operator import truediv
from pygame import mixer
import pygame, sys, random, time, math


#INICIADOR MÚSICA
mixer.init()
#INICIADOR FUENTE
pygame.font.init()
#INICIADOR PYGAME
pygame.init()
#COLORES
cafe=(115,60,29)
cafeN=(56,25,9)
verde_pasto=(0,58,15)
rosa_pastel=(255, 154, 162)
rosa_pastel_oscurito=(204, 143, 148)
rosa_pastel_oscuro=(201, 153, 175)
rosa_pastel_bajo=(222, 110, 106)
celeste_pastel=(179, 255, 255)
blanco_pastel=(255, 255, 216)
verde=(43, 153, 53)
azul_pastel=(71, 98, 165)
rojo_pastel=(255, 105, 97)
rojo_pastell=(218, 247, 166)
morado_pastel=(204, 169, 221)
naranja_pastel=(82, 245, 196)
atardecer=(253, 223, 126)
verde_oscuro=(45, 87, 44)
verde2=(189, 174, 110)
negro=(0, 0, 0)
color_piso=cafe
#RESOLUCIÓN VENTANA DE JUEGO
anchura=800
altura=400



frases_feas=["Prueba abrir los ojos", "Una vuelta mas a la manzana", "Hoy podría ser el día", "Son solo 4 botones", "¡Tú Puedes!", "¡Excelente Trabajo!", "Vamos, una vez mas", "¿Nota superior?", "¡Lo intentamos!", "...Jhon estuvo aquí..."]
frase_escoger=random.choice(frases_feas)

#LÓGICA LLUVIA

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
salud=100

#escoger número de canales
mixer.set_num_channels(20)


#capción de la ventana
pantalla=pygame.display.set_mode([anchura, altura])
pygame.display.set_caption('Cube Jumper')
fondo= celeste_pastel


fps=60
font = pygame.font.Font('fuentes/font2.otf', 15)
temporizador=pygame.time.Clock()

#cargar imagen
fondo1="fondo1.png"
fondote=fondo1
fondo2="fondo2.png"
fondo3="fondo3.png"
fondo4="fondo4.png"
    
bg = pygame.image.load(fondo1).convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()
scroll = 0
tiles = math.ceil(anchura  / bg_width) + 1



funcionar=True

#carga de fps y dibujado en pantalla
while funcionar:
    
    temporizador.tick(fps)
    for i in range(0, tiles):
        pantalla.blit(bg, (i * bg_width + scroll, 0))
        bg_rect.x = i * bg_width + scroll
        #pygame.draw.rect(pantalla, (255, 0, 0), bg_rect, 1)
    if activo:    

        scroll -= 3

        if abs(scroll) > bg_width:
            scroll = 0
    
    if not activo:
        #fuentes de pantalla
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
    

    #loop principal
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            funcionar=False
        if event.type==pygame.KEYDOWN and not activo:
            if event.key == pygame.K_UP:
                mixer.music.load('Skyarenastageidle.wav')
                mixer.music.play(-1)

                activo=True
                salud=1000
                jugador_x = 50
                puntaje = 0
                obstaculos= [890, 1000, 1500, 2000, 2500, ]
                obstaculo_velocidad = 3
                bg = pygame.image.load(fondo1).convert()
                color_piso=cafe
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

    if puntaje < 10:
        obstaculo0 = pygame.draw.rect(pantalla, rojo_pastell, [obstaculos[0], 200, 20, 20])
        obstaculo1 = pygame.draw.rect(pantalla, morado_pastel, [obstaculos[1], 200, 20, 20])
        obstaculo2 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[2], 200, 20, 20])
        obstaculo3 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[3], 200, 20, 20])
        obstaculo4 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[4], 200, 20, 20])
        bg = pygame.image.load(fondo1).convert()
        
        

    for i in range(len(obstaculos)):
        if activo:
            

            obstaculos[i] -= obstaculo_velocidad
            if obstaculos[i] < -20:
                obstaculos[i] = random.randint(800, 1500)
                puntaje += 1
            if puntaje == 10:
                color_piso=cafeN
                obstaculo_velocidad = 4
                bg = pygame.image.load(fondo2).convert()
                
            if puntaje >=10 and puntaje<30:
                obstaculo0 = pygame.draw.rect(pantalla, rojo_pastell, [obstaculos[0], 180, 20, 40])
                obstaculo1 = pygame.draw.rect(pantalla, morado_pastel, [obstaculos[1], 180, 20, 40])
                obstaculo2 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[2], 180, 20, 40])
                obstaculo3 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[3], 180, 20, 40])
                obstaculo4 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[4], 180, 20, 40])
                
                

            if puntaje > 50:

                obstaculo0 = pygame.draw.circle(pantalla, negro, (obstaculos[0], 200), 10)
                obstaculo1 = pygame.draw.circle(pantalla, negro, (obstaculos[1], 200), 10)
                obstaculo2 = pygame.draw.circle(pantalla, negro, (obstaculos[2], 200), 10)
                obstaculo3 = pygame.draw.circle(pantalla, negro, (obstaculos[3], 200), 10)
                obstaculo4 = pygame.draw.circle(pantalla, negro, (obstaculos[4], 200), 10)
                for j in lista_coordenadas:
                    

                    x = j[0]
                    y = j[1]
                    pygame.draw.line(pantalla, azul_pastel, (x, y), (x, y), 2)
                    j[1] +=1
                    if j[1] > 500:
                        j[1] = 0
            if puntaje == 30:
                obstaculo_velocidad = 5
                bg = pygame.image.load(fondo3).convert()
                color_piso=negro
            if puntaje >= 30 and puntaje <50:
                obstaculo0 = pygame.draw.rect(pantalla, rojo_pastell, [obstaculos[0], 200, 40, 20])
                obstaculo1 = pygame.draw.rect(pantalla, morado_pastel, [obstaculos[1], 200, 40, 20])
                obstaculo2 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[2], 200, 40, 20])
                obstaculo3 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[3], 200, 40, 20])
                obstaculo4 = pygame.draw.rect(pantalla, naranja_pastel, [obstaculos[4], 200, 40, 20])
            if puntaje == 50:
                obstaculo_velocidad = 9
                color_piso=verde_pasto
                mixer.music.load('skyarenafinal.wav')
                mixer.music.play(-1)
                bg = pygame.image.load(fondo4).convert()

                
                
                

            if jugador.colliderect(obstaculo0) or jugador.colliderect(obstaculo1) or jugador.colliderect(obstaculo2) or jugador.colliderect(obstaculo3) or jugador.colliderect(obstaculo4):
                
                salud= salud-1
                
                

            if salud == 0:
                mixer.music.stop()
                morir=mixer.Sound('Muerte.mp3')
                morir.play()
                activo = False

    #lógica de salto
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


