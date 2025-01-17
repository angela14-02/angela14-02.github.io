import pygame
import time
import random
import sys
import os

# Inicializar Pygame
pygame.init()

tamaño_bloque = 20

def obtener_ruta_recurso(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Configuración de la pantalla
ancho, alto = 600, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake Game")
asset_background = obtener_ruta_recurso('images/imagenes/fondo.jpg')
background = pygame.image.load(asset_background)
background = pygame.transform.scale(background, (ancho, alto))

# Cargar imagen de cabeza
cabezaizquierda = obtener_ruta_recurso('images/imagenes/cabeza-izquierda.png')
cabeza_background1 = pygame.image.load(cabezaizquierda)
cabeza_background1 = pygame.transform.scale(cabeza_background1, (tamaño_bloque, tamaño_bloque))
cabezaderecha = obtener_ruta_recurso('images/imagenes/cabeza-derecha.png')
cabeza_background2 = pygame.image.load(cabezaderecha)
cabeza_background2 = pygame.transform.scale(cabeza_background2, (tamaño_bloque, tamaño_bloque))
cabezaarriba = obtener_ruta_recurso('images/imagenes/cabeza-arriba.png')
cabeza_background3 = pygame.image.load(cabezaarriba)
cabeza_background3 = pygame.transform.scale(cabeza_background3, (tamaño_bloque, tamaño_bloque))
cabezaabajo = obtener_ruta_recurso('images/imagenes/cabeza-abajo.png')
cabeza_background4 = pygame.image.load(cabezaabajo)
cabeza_background4 = pygame.transform.scale(cabeza_background4, (tamaño_bloque, tamaño_bloque))

#Cargar imagen de comida
comida = obtener_ruta_recurso('images/imagenes/manzana.png')
cargarcomida = pygame.image.load(comida)
cargarcomida = pygame.transform.scale(cargarcomida, (tamaño_bloque, tamaño_bloque))

#Cargar sonido al comer
sonido_comer = obtener_ruta_recurso('images/imagenes/comer.mp3')
comer_sonido = pygame.mixer.Sound(sonido_comer)

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul_claro = (173, 216, 230)

# Tamaño de los bloques
tamaño_bloque = 20
velocidad = 10

# Fuente para el marcador
fuente = pygame.font.SysFont("Courier", 24)

# Función para mostrar el marcador
def mostrar_marcador(puntaje, record):
    texto = fuente.render(f"Score: {puntaje}    High Score: {record}", True, negro)
    pantalla.blit(texto, [10, 10])

# Función para generar comida en una posición válida
def generar_comida(cuerpo_serpiente):
    while True:
        comida_x = random.randint(0, (ancho // tamaño_bloque) - 1) * tamaño_bloque
        comida_y = random.randint(0, (alto // tamaño_bloque) - 1) * tamaño_bloque
        if [comida_x, comida_y] not in cuerpo_serpiente:  # Asegurarse de que la comida no esté en el cuerpo
            return comida_x, comida_y

# Función principal del juego
def juego():
    # Variables de la serpiente
    x = ancho // 2
    y = alto // 2
    dx = 0
    dy = 0
    evento1 = "abajo"

    cuerpo_serpiente = []
    longitud_serpiente = 1

    # Comida
    comida_x, comida_y = generar_comida(cuerpo_serpiente)

    # Marcadores
    score = 0
    high_score = 0

    # Bucle del juego
    reloj = pygame.time.Clock()
    juego_terminado = False

    while not juego_terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_terminado = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and dy == 0:
                    evento1 = "arriba"
                    dx, dy = 0, -tamaño_bloque
                if evento.key == pygame.K_DOWN and dy == 0:
                    evento1 = "abajo"
                    dx, dy = 0, tamaño_bloque
                if evento.key == pygame.K_LEFT and dx == 0:
                    evento1 = "izquierda"
                    dx, dy = -tamaño_bloque, 0
                if evento.key == pygame.K_RIGHT and dx == 0:
                    evento1 = "derecha"
                    dx, dy = tamaño_bloque, 0

        # Actualizar posición de la serpiente
        x += dx
        y += dy

        # Revisar colisiones con los bordes
        if x < 0 or x >= ancho or y < 0 or y >= alto:
            juego_terminado = True

        # Revisar colisiones con el propio cuerpo
        for bloque in cuerpo_serpiente[:-1]:
            if bloque == [x, y]:
                juego_terminado = True

        # Dibujar fondo
        pantalla.fill((0, 0, 0))
        pantalla.blit(background, (0, 0))

        # Dibujar comida
        pantalla.blit(cargarcomida, [comida_x, comida_y])

        # Dibujar la serpiente
        cabeza = [x, y]
        cuerpo_serpiente.append(cabeza)
        if len(cuerpo_serpiente) > longitud_serpiente:
            del cuerpo_serpiente[0]

        for i, bloque in enumerate(cuerpo_serpiente):
            if i == len(cuerpo_serpiente) - 1:  # Si es la cabeza
                if evento1 == "izquierda":
                    pantalla.blit(cabeza_background1, [bloque[0], bloque[1]])
                elif evento1 == "derecha":
                    pantalla.blit(cabeza_background2, [bloque[0], bloque[1]])
                elif evento1 == "arriba":
                    pantalla.blit(cabeza_background3, [bloque[0], bloque[1]])
                elif evento1 == "abajo":
                    pantalla.blit(cabeza_background4, [bloque[0], bloque[1]])
            else:  # Dibujar el cuerpo
                pygame.draw.rect(pantalla, negro, [bloque[0], bloque[1], tamaño_bloque, tamaño_bloque])

        # Comprobar si la serpiente come la comida
        if x == comida_x and y == comida_y:
            comida_x, comida_y = generar_comida(cuerpo_serpiente)
            longitud_serpiente += 1
            score += 1
            comer_sonido.play()
            if score > high_score:
                high_score = score

        # Mostrar marcador
        mostrar_marcador(score, high_score)

        # Actualizar pantalla y controlar la velocidad
        pygame.display.update()
        reloj.tick(velocidad)

    # Mensaje de fin
    pantalla.fill(negro)
    mensaje = fuente.render("Juego terminado.", True, blanco)
    mensaje = fuente.render("Presiona Q para salir.", True, blanco)
    pantalla.blit(mensaje, [ancho // 6, alto // 2])
    pygame.display.update()

    # Esperar a que el jugador presione Q para salir
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_q:
                pygame.quit()
                quit()

# Iniciar el juego
juego()


