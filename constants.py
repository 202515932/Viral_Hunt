import pygame
pygame.init()
FPS = 60 # cuántas veces por segundo se actualiza la pantalla.

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 
DARK_RED = (100, 0, 0)

# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILES = 3 # numero de imagenes que vas a formar parte del scroll infinito

# Screen limits
SCREEN_LOWER_LIMIT = 636
SCREEN_UPPER_LIMIT = 100

# Speed limit
GERM_SPEED_LOWER_LIMIT = [8, 15, 0, 10]
GERM_SPEED_UPPER_LIMIT = [12, 20, 0, 15]

VIRUS_X_SPEED_LOWER_LIMIT = [12, 0, 15, 0]
VIRUS_X_SPEED_UPPER_LIMIT = [18, 0, 20, 0]
VIRUS_Y_SPEEDS = [-3, -2, 2, 3]

OBSTACLE_SPEED_LOWER_LIMIT = [0, 8, 5, 5]
OBSTACLE_SPEED_UPPER_LIMIT = [0, 12, 10, 10]

BULLET_SPEED = 10

# Frequency
GERM_FREQUENCY = [10, 12, 99, 8]
VIRUS_FREQUENCY = [15, 99, 8, 99]
OBSTACLE_FREQUENCY = [99, 15, 55, 40]
BULLET_COLLDOWN_TIME = 250 

# FONT
GAME_OVER_TITLE = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 90)
FONT_TITLE = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 85)
FONT_SUBTITLE = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 40)
FONT_TEXT = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 18)

LEVEL_NAMES = ["TORRENTE SANGUINEO", "       PULMONES", "        CEREBRO", "        ESTOMAGO"]