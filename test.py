import pygame
import functions.funciones_nanobot as fn
import functions.funciones_general as fg
from constants import *

def test_bullet_generator():
    nanobot_rect = pygame.Rect(100, 200, 50, 50)
    bullet_image = pygame.Surface((10, 5))

    bullet = fn.bullet_generator(nanobot_rect, bullet_image)
    bullet_rect = bullet[0]

    if bullet_rect.midleft == nanobot_rect.midright:
        print(f"- BULLET GENERATOR - OK")
    else:
        print(f"- BULLET GENERATOR - ERROR")

def test_background_scroll_reset(screen):
        background = pygame.Surface((800, 600))
        background_width = background.get_width()

        scroll = -background_width - 10 # El fondo ya se desplazó más allá de su ancho, la funcion debe devolver un scroll = 0 (reiniciar scroll).
        new_scroll = fg.background_surface_scroll(scroll, screen, background, background_width)

        if new_scroll == 0:
            print(f"- BACKGROUND SCROLL RESET - OK")
        else:
            print(f"- BACKGROUND SCROLL RESET - ERROR")

def test_nanobot_collision():
                              # x  y  width  height
    nanobot_rect = pygame.Rect(100, 100, 50, 50)
    germ_rect = pygame.Rect(100, 100, 50, 50)
    germs = [[germ_rect, 3]]
    viruses = []
    obstacles = []

    game_over_sound = pygame.mixer.Sound("assets/sound/game_over.wav")
    game_over = False
    result = fn.nanobot_collisions(nanobot_rect, germs, viruses, obstacles, game_over, game_over_sound)
    if result:
        print(f"- NANOBOT COLLISION - OK")
    else:
        print(f"- NANOBOT COLLISION - ERROR")

def test_bullet_collision(screen):
    bullet_image = pygame.image.load("assets/images/Bala.png")
    bullet_rect = pygame.Rect(100, 100, 50, 50)
    bullets = [[bullet_rect, 3]]

    virus_rect = pygame.Rect(100, 100, 50, 50)
    viruses = [[virus_rect, 3]]

    dead_germ_sound = pygame.mixer.Sound("assets/sound/bacteria_muerta.mp3")
    germs = []
    score = 0

    score = fn.bullets_movement_collisions(bullets, germs, viruses, screen, bullet_image, dead_germ_sound, score)

    if score == 3:
        print(f"- BULLET COLLISION - OK")
    else:
        print(f"- BULLET COLLISION - ERROR")

if __name__ == "__main__":
    screen = pygame.Surface((SCREEN_WIDTH, 600))

    print(f"{"-"*50}\nTEST RUNNING...\n")

    test_bullet_generator()
    test_background_scroll_reset(screen)
    test_nanobot_collision()
    test_bullet_collision(screen)

    print(f"\nTEST FINISHED\n{"-"*50}")