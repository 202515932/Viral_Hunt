import pygame
from pygame.locals import *
import functions.funciones_general as fg
from constants import *

def create_main_menu(screen: pygame.Surface, clock: pygame.time.Clock) -> None:
    """
    Se crea y gestiona el menú principal del juego. Se da tres opciones de acciones a realizar: iniciar el juego, ver las instrucciones y salir del juego

    Args:
        screen (pygame.Surface): Superficie principal del juego.
        clock (pygame.time.Clock): Reloj para controlar los FPS.
    """

    background_menu = pygame.image.load("assets/images/Fondo_menu.png")

    # BOTONES DE LAS POSIBLES ACCIONES
    title_text = FONT_TITLE.render("VIRAL HUNT", True, WHITE)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2 + 50, 250))

    play_text = FONT_SUBTITLE.render("PLAY", True, WHITE)
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, 350))

    quit_text = FONT_SUBTITLE.render("QUIT", True, WHITE)
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, 475))

    instructions_text = FONT_SUBTITLE.render("INSTRUCTIONS", True, WHITE)
    instructions_rect = instructions_text.get_rect(center=(SCREEN_WIDTH // 2, 412))

    menu = True
    while menu:
        screen.blit(background_menu, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        if play_rect.collidepoint(mouse_pos):
            play_color = GREEN 
        else:
            play_color = WHITE
        
        if quit_rect.collidepoint(mouse_pos):
            quit_color = GREEN 
        else:
            quit_color = WHITE

        if instructions_rect.collidepoint(mouse_pos):
            instructions_color = GREEN
        else:
            instructions_color = WHITE

        play_text = FONT_SUBTITLE.render("PLAY", True, play_color)
        quit_text = FONT_SUBTITLE.render("QUIT", True, quit_color)
        instructions_text = FONT_SUBTITLE.render("INSTRUCTIONS", True, instructions_color)

        screen.blit(title_text, title_rect)
        screen.blit(play_text, play_rect)
        screen.blit(quit_text, quit_rect)
        screen.blit(instructions_text, instructions_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fg.terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    return  # Start game
                elif quit_rect.collidepoint(event.pos):
                    fg.terminate()
                elif instructions_rect.collidepoint(event.pos):
                    create_instruction_menu(clock, screen, background_menu)

        pygame.display.update()
        clock.tick(FPS)

def create_instruction_menu(clock: pygame.time.Clock, screen: pygame.Surface, background_menu: pygame.Surface) -> None:
    """
    Muestra el menú de instrucciones del juego donde se explica los controles básicos y se permite volver al menú principal.

    Args:
        clock (pygame.time.Clock): Reloj para controlar los FPS.
        screen (pygame.Surface): Superficie principal del juego.
        background_menu (pygame.Surface): Fondo del menú.
    """
     
    exit = False

    return_text = FONT_SUBTITLE.render("RETURN", True, WHITE)
    return_rect = return_text.get_rect(center=(SCREEN_WIDTH//2, 550))

    up_key = pygame.image.load("assets/images/up_key.png")
    w_key = pygame.image.load("assets/images/w_key.png")

    down_key = pygame.image.load("assets/images/down_key.png")
    s_key = pygame.image.load("assets/images/s_key.png")

    space_key = pygame.image.load("assets/images/space_key.png")

    while not exit:
        intruction_text(screen, background_menu, up_key, w_key, down_key, s_key, space_key)
        mouse_pos = pygame.mouse.get_pos()
        if return_rect.collidepoint(mouse_pos):
            return_color = GREEN
        else:
            return_color = WHITE
        
        return_text = FONT_SUBTITLE.render("RETURN", True, return_color)
        screen.blit(return_text, return_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fg.terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if return_rect.collidepoint(event.pos):
                    exit = False
                    return  
                
        pygame.display.update()
        clock.tick(FPS)

def intruction_text(screen: pygame.Surface, background_menu: pygame.Surface, up_key: pygame.Surface, w_key: pygame.Surface, down_key: pygame.Surface, s_key: pygame.Surface, space_key: pygame.Surface) -> None:
    """
    Dibuja en pantalla los textos e imágenes de las instrucciones.

    Args:
        screen (pygame.Surface): Superficie principal del juego.
        background_menu (pygame.Surface): Imagen de fondo.
        up_key (pygame.Surface): Imagen de la tecla flecha arriba.
        w_key (pygame.Surface): Imagen de la tecla W.
        down_key (pygame.Surface): Imagen de la tecla flecha abajo.
        s_key (pygame.Surface): Imagen de la tecla S.
        space_key (pygame.Surface): Imagen de la barra espaciadora.
    """
    
    screen.blit(background_menu, (0, 0))
    title_text = FONT_SUBTITLE.render("INSTRUCTIONS", True, WHITE)
    screen.blit(title_text, (SCREEN_WIDTH // 3 - 20, SCREEN_HEIGHT // 5))

    go_up_text = FONT_SUBTITLE.render("- Press   or   to go UP", True, WHITE)
    screen.blit(go_up_text,(160, 220))
    screen.blit(up_key,(470, 220))
    screen.blit(w_key,(670, 220))

    go_down_text = FONT_SUBTITLE.render("- Press   or   to go DOWN", True, WHITE)
    screen.blit(go_down_text,(160, 320))
    screen.blit(down_key,(470, 320))
    screen.blit(s_key,(670, 320))

    space_text = FONT_SUBTITLE.render("- Press         to SHOT", True, WHITE)
    screen.blit(space_text,(160, 420))
    screen.blit(space_key, (460, 420))