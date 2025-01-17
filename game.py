import pygame
import random
import math
import sys
import os

# Inicializar pygame
pygame.init()

# Estable el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Función para obtener la ruta de los recursos
def obtener_ruta_recurso(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Cargar imagen de fondo
asset_background = obtener_ruta_recurso('assets/images/background.png')
background = pygame.image.load(asset_background)

# Cargar icono de ventana
asset_icon = obtener_ruta_recurso('assets/images/ufo.png')
icon = pygame.image.load(asset_icon)

# Cargar sonido de fondo
asset_sound = obtener_ruta_recurso('assets/audios/background_music2.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

# Cargar sonido de disparo
asset_sound3 = obtener_ruta_recurso('assets/audios/disparar.mp3')
disparo_sonido = pygame.mixer.Sound(asset_sound3)

# Cargar sonido de colisión
asset_sound2 = obtener_ruta_recurso('assets/audios/colision.mp3')
colision_sonido = pygame.mixer.Sound(asset_sound2)

# Cargar sonido de game over
asset_sound4 = obtener_ruta_recurso('assets/audios/gameover.mp3')
gameover_sonido = pygame.mixer.Sound(asset_sound4)

# Cargar imagen del jugador
asset_playerimg = obtener_ruta_recurso('assets/images/space-invaders.png')
playerimg = pygame.image.load(asset_playerimg)

# Cargar imagen de bala
asset_bulletimg = obtener_ruta_recurso('assets/images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

# Cargar imagen de meteorito
asset_meteorimg = obtener_ruta_recurso('assets/images/meteor.png')
meteorimg = pygame.image.load(asset_meteorimg)
meteorimg = pygame.transform.scale(meteorimg, (91, 91))

# Cargar fuente para texto de game over
asset_over_font = obtener_ruta_recurso('assets/fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font, 64)

# Cargar fuente para texto de puntaje
asset_font = obtener_ruta_recurso('assets/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font, 32)

# Establecer título de ventana
pygame.display.set_caption("Space Invader")

# Establecer icono de ventana
pygame.display.set_icon(icon)

# Reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

# Crear reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Variables globales del jugador
playerx = 370
playery = 470
playerx_change = 0

# Variables globales de las balas
bullets = []  # Lista para almacenar las balas activas
bullet_speed = 10

# Variables globales de los enemigos
enemyimg = []
enemyY = []
enemyX = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

# Inicializar posiciones de los enemigos
for i in range(no_of_enemies):
    enemy1 = obtener_ruta_recurso('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))

    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))

    enemyX_change.append(5)
    enemyY_change.append(20)

# Variables globales de los meteoritos
meteorX = []
meteorY = []
meteorY_change = []
no_of_meteors = 5

# Inicializar posiciones de los meteoritos
for i in range(no_of_meteors):
    meteorX.append(random.randint(0, 736))
    meteorY.append(random.randint(-600, -50))
    meteorY_change.append(random.randint(3, 7))

# Puntuación
score = 0

# Funciones auxiliares
def show_score():
    score_value = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (10, 10))
    return score

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

def meteor(x, y):
    screen.blit(meteorimg, (x, y))

def fire_bullet(x, y):
    disparo_sonido.play()
    bullets.append({"x": x + 16, "y": y})

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    return distance < 27

def isCollisionMeteor(playerX, playerY, meteorX, meteorY):
    distance = math.sqrt((math.pow(playerX - meteorX, 2)) + (math.pow(playerY - meteorY, 2)))
    return distance < 30

def game_over_text(score):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(int(screen_width / 2), int(screen_height / 3)))
    screen.blit(over_text, text_rect)

    restart_text = font.render("Press R to Restart", True, (255, 255, 255))
    restart_rect = restart_text.get_rect(center=(int(screen_width / 2), int(screen_height / 3) + 50))
    screen.blit(restart_text, restart_rect)

    score_text = over_font.render(str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(int(screen_width / 2), int(screen_height / 3) + 100))
    screen.blit(score_text, score_rect)

def restart_game():
    global playerx, playery, playerx_change, bullets, score
    global enemyX, enemyY, enemyX_change, enemyY_change
    global meteorX, meteorY, meteorY_change

    playerx = 370
    playery = 470
    playerx_change = 0

    bullets.clear()
    score = 0

    for i in range(no_of_enemies):
        enemyX[i] = random.randint(0, 736)
        enemyY[i] = random.randint(0, 150)
        enemyX_change[i] = 5
        enemyY_change[i] = 20

    for i in range(no_of_meteors):
        meteorX[i] = random.randint(0, 736)
        meteorY[i] = random.randint(-600, -50)
        meteorY_change[i] = random.randint(3, 7)

# Bucle principal
in_game = True
game_over = False
while in_game:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            in_game = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT:
                    playerx_change = -5
                if event.key == pygame.K_RIGHT:
                    playerx_change = 5
                if event.key == pygame.K_SPACE:
                    fire_bullet(playerx, playery)

            if game_over and event.key == pygame.K_r:
                game_over = False
                restart_game()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0

    if not game_over:
        playerx += playerx_change
        if playerx <= 0:
            playerx = 0
        elif playerx >= 736:
            playerx = 736

        for i in range(no_of_enemies):
            if enemyY[i] > 440:
                gameover_sonido.play()
                game_over = True

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            for bullet in bullets[:]:
                if isCollision(enemyX[i], enemyY[i], bullet["x"], bullet["y"]):
                    colision_sonido.play()
                    bullets.remove(bullet)
                    score += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(0, 150)
                    break

            enemy(enemyX[i], enemyY[i], i)

        for i in range(no_of_meteors):
            meteorY[i] += meteorY_change[i]
            if meteorY[i] > 600:
                meteorY[i] = random.randint(-600, -50)
                meteorX[i] = random.randint(0, 736)

            if isCollisionMeteor(playerx, playery, meteorX[i], meteorY[i]):
                gameover_sonido.play()
                game_over = True

            meteor(meteorX[i], meteorY[i])

        for bullet in bullets[:]:
            bullet["y"] -= bullet_speed
            if bullet["y"] < 0:
                bullets.remove(bullet)
            else:
                screen.blit(bulletimg, (bullet["x"], bullet["y"]))

        player(playerx, playery)
        show_score()
    else:
        game_over_text(score)

    pygame.display.update()
    clock.tick(120)
