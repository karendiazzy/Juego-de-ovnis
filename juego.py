
import pygame
from pygame import KEYDOWN
import random
import math
# Inicializo a pygame
pygame.init()
# Creamos pantalla del juego
pantalla = pygame.display.set_mode((800,600))
# Cambio el iconno del juego
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load("C:/Users/karen/OneDrive/Escritorio/Certificacion Python/pythonProject/Juego de ovni/ufo.png")
pygame.display.set_icon(icono)

#variables de jugador :)
img_jugador = pygame.image.load("C:/Users/karen/OneDrive/Escritorio/Certificacion Python/pythonProject/Juego de ovni/rocket.png")
jugador_X = 368  #medida donde quiero que valla el cohetito
jugador_Y = 500  #medida donde quiero que valla el cohetito
jugador_x_cambio = 0

#variables del enemigo :(
img_enemigo = []
enemigo_X = []
enemigo_Y = []
enemigo_x_cambio = []
enemigo_Y_cambio = []
cantidad_enemigos = 5

for enemiguito in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("C:/Users/karen/OneDrive/Escritorio/Certificacion Python/pythonProject/Juego de ovni/ufo (1).png"))
    enemigo_X.append(random.randint(0,736))  #medida donde quiero que valla el enemigo que sea aleatoria :)
    enemigo_Y.append(random.randint(50,200)) #medida donde quiero que valla el enemigo
    enemigo_x_cambio.append(0.3)
    enemigo_Y_cambio.append(50)
    
#variables de la bala
img_bala = pygame.image.load("C:/Users/karen/OneDrive/Escritorio/Certificacion Python/pythonProject/Juego de ovni/bala.png")
bala_X =  0
bala_Y = 500
bala_x_cambio = 0 #no se usa
bala_Y_cambio = 3
bala_visible =False

#puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32) #"freesansbold.ttf" es una fuente predeterminada de pygame
texto_y = 10
texto_x = 10

#texto final
texto_final= pygame.font.Font("freesansbold.ttf" , 40)
#funcion para finalizar el juego
def texto_final():
    fuente_final = texto_final.render("¡OH OH! **PERDISTE** :(  __TU JUEGO A TERMINADO__", True, (255,255,255))
    pantalla.blit(fuente_final , (60, 200)) #numeros que representan la posicion de la pantalla
    
#funcion de mostrar el puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}" , True , (255,255,255)) #render quiere decir renderizar o imprimir en pantalla
    pantalla.blit(texto, (x,y))                                      #recordar que el color se elige con los 3 primarios

 #Funcion de jugador
def jugador (x,y):
    pantalla.blit(img_jugador, (x, y))
    
 #Funcion de enemigo
def enemigo (x,y , ene):
    pantalla.blit(img_enemigo[ene], (x+16, y+10))
    
#Funcion disparar bala
def disparar(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x,y))
    
# funcion para calcular colisciones
def hay_colision(x1,y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia <27:
        return True
    else:
        return False

#loop del juego
se_ejecuta = True
while se_ejecuta:
    pantalla.fill((205,144,220)) #Pide 3 numeros que representan los 3 colores primarios, hay de 1 a 250 en cada color PUEDO ENTRAR A LA PAGINA WEB "COLORSPIRE"
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #mover con flecha derecha o izquierda la nave  
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:  
                jugador_x_cambio = -1 #si pongo 1 se mueve lento, con 3 se mueve mas rapido
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1  #si pongo 1 se mueve lento, con 3 se mueve mas rapido
            #disparar bala
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_X = jugador_X
                    disparar(bala_X,bala_Y)
        # detener la nave al dejar de presionar la tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
           
    #modificar la ubicacion del jugador_______________________________________________
    jugador_X += jugador_x_cambio 
    #mantener dentro de los bordes del jugador
    if jugador_X <= 0:
        jugador_X = 0
    elif jugador_X >= 736: #el eje x tiene hasta 800 pixeles, y la nave tiene 64 pixel, entonces calculamos restamos 800-64 eso nos da 736
        jugador_X =736
    #________________________________________________________________________________
    #modificar la ubicacion del Enemigo
    for enemiguito in range(cantidad_enemigos):
        #fin del juego
        if enemigo_Y[enemiguito]>455:
            for k in range(cantidad_enemigos):
                enemigo_Y[k] = 1000
            texto_final()
            break
        
        
        enemigo_X[enemiguito] += enemigo_x_cambio[enemiguito]
    #mantener dentro de los bordes del Enemigo
        if enemigo_X[enemiguito] <= 0:
            enemigo_x_cambio[enemiguito] = 0.3
            enemigo_Y[enemiguito] += enemigo_Y_cambio[enemiguito]
        elif enemigo_X[enemiguito] >=736: 
            enemigo_x_cambio[enemiguito] = -0.3
            enemigo_Y[enemiguito] += enemigo_Y_cambio[enemiguito]
        #colision
        colision = hay_colision(enemigo_X[enemiguito] ,enemigo_Y[enemiguito] ,bala_X , bala_Y)
        if colision:
            bala_Y = 500
            bala_visible = False
            puntaje += 1
            enemigo_X[enemiguito] = random.randint(0,736)   
            enemigo_Y[enemiguito] = random.randint(50,200)
        
        enemigo(enemigo_X[enemiguito] , enemigo_Y[enemiguito] , enemiguito) 
    #__________________________________________________________________________________    
    #movimiento de la bala
    if bala_Y <= -64:
        bala_Y = 500
        bala_visible = False
        
    if bala_visible:
        disparar(bala_X , bala_Y)
        bala_Y -= bala_Y_cambio
        
    #____________________________________________________________________________________
    jugador(jugador_X,jugador_Y)

    mostrar_puntaje(texto_x , texto_y)
    
    #Actualizamos cn update
    pygame.display.update()   

