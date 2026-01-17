import pygame
from pygame.locals import *
from constants import *

def nanobot_movement(rect_nanobot: pygame.Rect) -> None:
    """
    Realiza el movimiento vertical del nanobot según la entrada del teclado.
    El nanobot se mueve hacia arriba presionando (W / flecha hacia arriba) o hacia abajo usando (S / flecha hacia abajo).

    Args:
        rect_nanobot (pygame.Rect): Rectángulo que representa la posición y tamaño del nanobot.
    """

    key_pressed_down = pygame.key.get_pressed()
    if key_pressed_down[K_UP] or key_pressed_down[K_w]:
        rect_nanobot.move_ip(0, -5)
    if key_pressed_down[K_DOWN] or key_pressed_down[K_s]:
        rect_nanobot.move_ip(0, 5)

def nanobot_collisions(rect_nanobot: pygame.Rect, germs: list[list], viruses: list[list], obstacles: list[list], game_over: bool, game_over_sound: pygame.mixer.Sound) -> bool:
    """
    Detecta y gestiona (invocando terminate() y repoduciendo el sonido correspondiente) las colisiones del nanobot con enemigos u obstaculos
    
    Args:
        rect_nanobot (pygame.Rect): Rectángulo que representa la posición y tamaño del nanobot.
        germs (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los germenes activos
        viruses (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los virus activos
        obstacles (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los obstaculos activos
        game_over (bool): Indica si el jugador ha perdido.
        game_over_sound (pygame.mixer.Sound): sonido de game over

    Return:
        game_over (bool): Indica el nuevo estado del jugador, si ha perdido o no.
    """

    for germ in germs:  
        rect_germ = germ[0]
        if rect_nanobot.colliderect(rect_germ):
                game_over = True
                pygame.mixer.music.pause()
                game_over_sound.play()

    for virus in viruses:
        rect_virus = virus[0]
        if rect_nanobot.colliderect(rect_virus):
                game_over = True
                pygame.mixer.music.pause()
                game_over_sound.play()

    for obstacle in obstacles:
        rect_obstacle = obstacle[0]
        if rect_nanobot.colliderect(rect_obstacle):
            game_over = True
            game_over_sound.play()

    return game_over

def bullet_generator(rect_nanobot: pygame.Rect, bullet_image: pygame.Surface) -> list:
    """
    Crea una bala posicionándo su lateral izquierdo en el lateral derecho del nanobot.

    Args:
        rect_nanobot (pygame.Rect): Rectángulo que representa la posición y tamaño del nanobot.
        bullet_image (pygame.Surface): Imagen de la bala.

    Returns:
        list: Lista que contiene el rectángulo de la bala y su imagen.
    """

    rect_bullet = bullet_image.get_rect()
    rect_bullet.midleft = rect_nanobot.midright
    return [rect_bullet, bullet_image]

def bullets_movement_collisions(bullets: list[list], germs: list[list], viruses: list[list], screen: pygame.Surface, bullet_image: pygame.Surface, dead_germ_sound: pygame.mixer.Sound, score: int) -> int:
    """
    Mueve las balas hacia la derecha de la pantalla y elimina estas cuando se salen de la pantalla, elimina gérmenes y virus al ser colisionados
    y actualiza la puntuación según el enemigo destruido (1pto por bacteria y 3ptos por virus).

    Args:
        bullets (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todas las balas activas
        germs (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los germenes activos
        viruses (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los virus activos
        screen (pygame.Surface): Superficie principal donde se dibuja el juego.
        bullet_image (pygame.Surface): Imagen de la bala.
        dead_germ_sound (pygame.mixer.Sound): Sonido al eliminar un enemigo.
        score (int): Puntuación actual.

    Returns:
        int: Nueva puntuación del jugador.
    """

    bullets_collided = []
    dead_germs = []
    dead_viruses = []

    for bullet in bullets:
        rect_bullet = bullet[0]
        rect_bullet.x += BULLET_SPEED
        screen.blit(bullet_image, rect_bullet)

        if rect_bullet.left > SCREEN_WIDTH:
            bullets_collided.append(bullet)

        for germ in germs:
            rect_germ = germ[0]
            if rect_bullet.colliderect(rect_germ):
                bullets_collided.append(bullet)
                dead_germs.append(germ)
                dead_germ_sound.play()
        
        for virus in viruses:
            rect_virus = virus[0]
            if rect_bullet.colliderect(rect_virus):
                bullets_collided.append(bullet)
                dead_viruses.append(virus)
                dead_germ_sound.play()

    for bullet_collided in bullets_collided:
        if bullet_collided in bullets:
            bullets.remove(bullet_collided)

    for dead_germ in dead_germs:
        if dead_germ in germs:
            score += 1
            germs.remove(dead_germ)

    for dead_virus in dead_viruses:
        if dead_virus in viruses:
            score += 3
            viruses.remove(dead_virus)
    return score