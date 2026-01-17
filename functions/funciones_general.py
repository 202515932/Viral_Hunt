import pygame
from sys import exit
from pygame.locals import *
from constants import *    

def terminate() -> None:
    """
    Finaliza la ejecución del programa y cierra el juego
    """
    pygame.quit()
    exit() 
                  
def background_surface_scroll(scroll: int, screen: pygame.Surface, background_ts: pygame.Surface, background_ts_width:int) -> int:
    """
    Desplaza horizontalmente el fondo del juego hacia la izquierda, una vez que el valor del scroll es mayor que el ancho de la pantalla 
    se vuelve a poner el scroll a cero para hacer un efecto de scroll infinito. Esto se hace con tres fondos indenticos a la vez.
    
    Args:
        scroll (int): Valor actual del desplazamiento del fondo.
        screen (pygame.Surface): Superficie principal donde se dibuja el juego.
        background_ts (pygame.Surface): Imagen del fondo.
        background_ts_width (int): Ancho de la imagen del fondo.

    Returns:
        int: Nuevo valor del desplazamiento del fondo.
    """
    for counter in range(0, TILES):
        screen.blit(background_ts, (counter * background_ts_width + scroll, 0))
    scroll -= 5
    if abs(scroll) > background_ts_width:
        scroll = 0
    return scroll

def game_over_text(screen: pygame.Surface, game_over: bool, game_time_passed: int, score: int, clock: pygame.time.Clock) -> None:
    """
    Muestra la pantalla de Game Over y la opción de reinicio del juego.

    Args:
        screen (pygame.Surface): Superficie principal del juego.
        game_over (bool): Indica si el jugador ha perdido.
        game_time_passed (int): Tiempo total jugado.
        score (int): Puntuación final del jugador.
        clock (pygame.time.Clock): Reloj del juego para controlar los FPS.
    """
    screen.fill(BLACK)
    game_over_text = GAME_OVER_TITLE.render("GAME OVER", True, DARK_RED)
    screen.blit(game_over_text, (SCREEN_WIDTH // 5 - 20, SCREEN_HEIGHT // 2 - 100))

    restart_text = FONT_SUBTITLE.render("RESTART", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 75))

    running = True
    while running:
        screen.fill(BLACK)
        screen.blit(game_over_text, (SCREEN_WIDTH // 5 - 20, SCREEN_HEIGHT // 2 - 100))
        display_score_and_time(game_time_passed, screen, game_over, score)   

        mouse_pos = pygame.mouse.get_pos()
        if restart_rect.collidepoint(mouse_pos):
            restart_color = GREEN
        else:
            restart_color = WHITE
        
        restart_text = FONT_SUBTITLE.render("RESTART", True, restart_color)
        screen.blit(restart_text, restart_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                terminate()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_rect.collidepoint(event.pos):
                    running = False
                    return 
                
        pygame.display.update()
        clock.tick(FPS)

def display_score_and_time(game_time_passed: int, screen: pygame.Surface, game_over: bool, score: int) -> None:
    """
    Muestra el tiempo que ha estado jugando y la puntuación del jugador en pantalla.

    game_time_passed (int): Tiempo total jugado.
    screen (pygame.Surface): Superficie principal del juego.
    game_over (bool): Indica si el jugador ha perdido.
    score (int): Puntuación final del jugador.
    """

    game_time_passed_text = f"DISTANCE: {str(int(game_time_passed/1000))}mm"
    game_score_text = f"SCORE: {str(score)}"
    if not game_over:
        game_time_passed_text = FONT_TEXT.render(game_time_passed_text, True, WHITE)
        screen.blit(game_time_passed_text, (50, 30))   
        game_score_text = FONT_TEXT.render(game_score_text, True, WHITE)
        screen.blit(game_score_text, (50, 60))  
    else:
        text = FONT_TEXT.render(f"{game_time_passed_text}    {game_score_text}", True, DARK_RED)
        screen.blit(text, (SCREEN_WIDTH // 3 - 20, SCREEN_HEIGHT // 2 )) 

def display_level(screen: pygame.Surface, level: int) -> None:
    """
    Muestra en pantalla el nombre del nivel actual del juego.

    Args:
        screen (pygame.Surface): Superficie principal del juego.
        level (int): Nivel actual del juego.
    """

    level_name = LEVEL_NAMES[level]
    level_name_text = FONT_TEXT.render(level_name, True, WHITE)
    screen.blit(level_name_text, (900, 45))