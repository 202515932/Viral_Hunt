import random
from pygame.locals import *
from constants import *

def generate_germ(germ_image: pygame.Surface, level: int) -> list:
    """
    Genera un nuevo germen con la posicion x en el limite derecho de la pantalla y una altura y velocidad aleatoria (dentro del rango establecido mediante constantes).

    Args:
        germ_image (pygame.Surface): Imagen del germen.
        level (int): Nivel actual del juego.

    Returns:
        list: Lista con el rectángulo (posición y tamaño) del germen y su velocidad.
    """

    rect_germ = germ_image.get_rect() 
    rect_germ.x = SCREEN_WIDTH 
    rect_germ.y = random.randint(SCREEN_UPPER_LIMIT, SCREEN_LOWER_LIMIT - 60)
    speed = random.randint(GERM_SPEED_LOWER_LIMIT[level], GERM_SPEED_UPPER_LIMIT[level])
    return [rect_germ, speed]

def germ_movement(germs:list[list], germ_image: pygame.Surface, screen: pygame.Surface, level: int) -> None:
    """
    Gestiona la generación, el movimiento y la eliminación de los gérmenes. Cuando el borde izquierdo de los germenes tiene la coordenada de x igual a cero estos son eliminados.

    Args:
        germs (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los germenes activos
        germ_image (pygame.Surface): Imagen del germen.
        screen (pygame.Surface): Superficie principal del juego.
        level (int): Nivel actual del juego.
    """

    if random.randint(1, GERM_FREQUENCY[level]) == 1:  
        germs.append(generate_germ(germ_image, level))

    for germ in germs:  
        rect_germ = germ[0]
        speed = germ[1]
        rect_germ.x -= speed
        screen.blit(germ_image, rect_germ)

        if rect_germ.left < 0:
            germs.remove(germ)

def generate_virus(virus_image: pygame.Surface, level: int) -> list:
    """
    Genera un nuevo virus con la posicion x en el limite derecho de la pantalla y una altura y velocidad aleatoria (dentro del rango establecido por constantes).
    Además se le introduce una velocidad en el sentido del eje y (vertical)

    Args:
        virus_image (pygame.Surface): Imagen del virus.
        level (int): Nivel actual del juego.

    Returns:
        list: Lista con el rectángulo (posición y tamaño) del virus y su velocidad horizontal y vertical.
    """

    rect_virus = virus_image.get_rect()
    rect_virus.x = SCREEN_WIDTH
    rect_virus.y = random.randint(SCREEN_UPPER_LIMIT, SCREEN_LOWER_LIMIT - 60)
    virus_speed_x = random.randint(VIRUS_X_SPEED_LOWER_LIMIT[level], VIRUS_X_SPEED_UPPER_LIMIT[level])  
    virus_speed_y = random.choice(VIRUS_Y_SPEEDS)  
    return [rect_virus, virus_speed_x, virus_speed_y]

def virus_movement(viruses: list[list], virus_image: pygame.Surface, screen: pygame.Surface, level: int) -> None:
    """
    Gestiona la generación, el movimiento y la eliminación de los virus. Cuando el borde izquierdo de los virus tiene la coordenada de x igual a cero estos son eliminados.
    Además, cuando el virus toca por la parte de arriba o por la parte de abajo los limites del area de juego establecido estos rebotan (se pone un negativo a su velocidad vertical)

    Args:
        viruses (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los virus activos
        virus_image (pygame.Surface): Imagen del virus.
        screen (pygame.Surface): Superficie principal del juego.
        level (int): Nivel actual del juego.
    """

    if random.randint(1, VIRUS_FREQUENCY[level]) == 1:
        viruses.append(generate_virus(virus_image, level))

    for virus in viruses:
        rect_virus = virus[0]
        virus_speed_x = virus[1]
        virus_speed_y = virus[2]

        rect_virus.x -= virus_speed_x
        rect_virus.y += virus_speed_y
        if rect_virus.bottom >= SCREEN_LOWER_LIMIT or rect_virus.top <= SCREEN_UPPER_LIMIT:
            virus[2] = -virus[2]

        screen.blit(virus_image, rect_virus)

        if rect_virus.left < 0:
            viruses.remove(virus)

def generate_obstacle(obstacle_image: pygame.Surface, level: int) -> list:
    """
    Genera un nuevo obstaculo con la posicion x en el limite derecho de la pantalla y una altura y velocidad aleatoria (dentro del rango establecido por constantes).

    Args:
        obstacle_image (pygame.Surface): Imagen del obstaculo.
        level (int): Nivel actual del juego.

    Returns:
        list: Lista con el rectángulo (posición y tamaño) del obstaculo y su velocidad.
    """

    rect_obstacle = obstacle_image.get_rect()
    rect_obstacle.x = SCREEN_WIDTH
    rect_obstacle.y = random.randint(SCREEN_UPPER_LIMIT, SCREEN_LOWER_LIMIT - 150)
    speed = random.randint(OBSTACLE_SPEED_LOWER_LIMIT[level], OBSTACLE_SPEED_UPPER_LIMIT[level])
    return [rect_obstacle, speed]

def obstacle_movement(obstacles: list[list], obstacle_image: pygame.Surface, screen: pygame.Surface, level: int) -> None:
    """
    Gestiona la generación, el movimiento y la eliminación de los obstaculos. Cuando el borde izquierdo de los obstaculos tiene la coordenada de x igual a cero estos son eliminados.

    Args:
        obstacles (list[list]): lista de listas que contiene la posicion/tamaño y velocidad de todos los obstaculos activos
        obstacle_image (pygame.Surface): Imagen del obstaculo.
        screen (pygame.Surface): Superficie principal del juego.
        level (int): Nivel actual del juego.
    """

    if random.randint(1, OBSTACLE_FREQUENCY[level]) == 1:
        obstacles.append(generate_obstacle(obstacle_image, level))
    
    for obstacle in obstacles:
        rect_obstacle = obstacle[0]
        speed = obstacle[1]
        rect_obstacle.x -= speed
        screen.blit(obstacle_image, rect_obstacle)
        
        if rect_obstacle.left < 0:
            obstacles.remove(obstacle)