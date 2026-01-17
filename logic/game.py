import pygame
from pygame.locals import *
import functions.funciones_general as fg
import functions.funciones_nanobot as fn
import functions.funciones_enemies as fe
from logic.menu import *
from constants import *

def game_loop(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    Bucle principal del juego donde se gestiona:
    - Carga de imagenes y audios para el juego
    - Lógica del juego
    - Detección de colisiones
    - Disparo y movimiento (del nanobot, enemigos y obstaculos)
    - Progresión de niveles
    - Pantalla de Game Over

    Args:
        screen (pygame.Surface): Superficie principal donde se dibuja el juego.
        clock (pygame.time.Clock): Reloj para controlar los FPS.
    """

    background_ts = pygame.image.load("assets/images/Fondo_torrente_sanguineo.jpg").convert()
    background_ts_width = background_ts.get_width()

    background_lungs = pygame.image.load("assets/images/fondo_pulmones.jpg")
    background_brain = pygame.image.load("assets/images/fondo_cerebro.png")
    background_stomach = pygame.image.load("assets/images/fondo_estomago.jpg")

    nanobot_image = pygame.image.load("assets/images/Nanobot.png")
    rect_nanobot = nanobot_image.get_rect()
    rect_nanobot.topleft = (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2) # Nanobot starts in the center
    
    germ_image = pygame.image.load("assets/images/Bacteria.png")
    flying_germ_image = pygame.image.load("assets/images/flying_germ.png")
    stomach_germ_image = pygame.image.load("assets/images/stomach_germ.png")
    germs = []

    virus_image = pygame.image.load("assets/images/Virus.png")
    electrical_virus = pygame.image.load("assets/images/virus_electrico.png")
    viruses = []

    obstacle_image = pygame.image.load("assets/images/toxic_cloud.png")
    electrical_obs_image = pygame.image.load("assets/images/impulso_electrico.png")
    food_obstacle_image = pygame.image.load("assets/images/restos_comida.png")
    obstacles = []

    bullet_image = pygame.image.load("assets/images/Bala.png")
    last_fired = 0
    bullets = []

    # sounds
    bullet_sound = pygame.mixer.Sound("assets/sound/disparo.wav")
    bullet_sound.set_volume(0.7)
    game_over_sound = pygame.mixer.Sound("assets/sound/game_over.wav")
    game_over_sound.set_volume(0.7)
    dead_germ_sound = pygame.mixer.Sound("assets/sound/bacteria_muerta.mp3")
    dead_germ_sound.set_volume(0.9)
    
    #pygame.mixer.music.load("assets/sound/musica_fondo.mp3")
    #pygame.mixer.music.set_volume(0.5)            
    #pygame.mixer.music.play(-1)  

    # game variables
    scroll = 0              
    run = True
    game_over = False
    score = 0
    time_game_started = pygame.time.get_ticks()
    level = 0

    while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if not game_over:
                game_time_passed = pygame.time.get_ticks() - time_game_started
                if game_time_passed > 30 * 1000 or score > 50:
                    level = 1
                    game_background = background_lungs
                    germ_image = flying_germ_image
                    viruses.clear()
                elif game_time_passed > 60 * 1000 or score > 100:
                    level = 2
                    game_background = background_brain
                    virus_image = electrical_virus  
                    obstacle_image = electrical_obs_image
                    germs.clear()
                elif game_time_passed > 90 * 1000 or score > 150:
                    level = 3
                    game_background = background_stomach
                    obstacle_image = food_obstacle_image
                    germ_image = stomach_germ_image
                    viruses.clear()

                else:
                    game_background = background_ts
                    obstacles.clear()

               
                scroll = fg.background_surface_scroll(scroll, screen, game_background, background_ts_width)

                # NANOBOT
                fn.nanobot_movement(rect_nanobot)           
                screen.blit(nanobot_image, rect_nanobot)
                if rect_nanobot.bottom >= SCREEN_LOWER_LIMIT or rect_nanobot.top <= SCREEN_UPPER_LIMIT: 
                    game_over = True

                # GERMS AND VIRUSES
                fe.germ_movement(germs, germ_image, screen, level)
                fe.virus_movement(viruses, virus_image, screen, level)
                fe.obstacle_movement(obstacles, obstacle_image, screen, level)

                # BULLETS                
                keys_pressed_dowm = pygame.key.get_pressed()
                
                if keys_pressed_dowm[K_SPACE]:
                    if game_time_passed - last_fired >= BULLET_COLLDOWN_TIME:
                            new_bullet =  fn.bullet_generator(rect_nanobot, bullet_image)
                            bullets.append(new_bullet)
                            last_fired = game_time_passed  # actualizar tiempo del último disparo
                            bullet_sound.play()

                score = fn.bullets_movement_collisions(bullets, germs, viruses, screen, bullet_image, dead_germ_sound, score)
                game_over = fn.nanobot_collisions(rect_nanobot, germs, viruses, obstacles, game_over, game_over_sound)
                fg.display_score_and_time(game_time_passed, screen, game_over, score)
                fg.display_level(screen, level)
           
            else:          
                fg.game_over_text(screen, game_over, game_time_passed, score, clock)
                return # restart game
                  
            pygame.display.update()    
            clock.tick(FPS)

    fg.terminate()