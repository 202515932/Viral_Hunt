import pygame
import logic.game as game
import logic.menu as menu
import logic.safety_check as safec
from constants import *

if __name__ == "__main__":
      safec.full_check()
      pygame.init()
      screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      pygame.display.set_caption("Viral Hunt")
      clock = pygame.time.Clock()

      menu.create_main_menu(screen, clock)
      
      while True:
            game.game_loop(screen, clock)