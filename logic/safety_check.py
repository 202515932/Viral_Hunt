import pygame
from logic.excepciones import *
import functions.funciones_general as fg

def check_fonts() -> None:
    """
    Comprueba que todas las fuentes listadas en el archivo de recursos existen
    y pueden cargarse correctamente con pygame.

    raises FontError: Si falta el archivo de listado o alguna fuente.
    """

    try:
        with open("assets/fonts/font_assets_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                path_to_check = line.strip()
                try:
                    pygame.font.Font(f"assets/fonts/{path_to_check}", 90)
                except FileNotFoundError as error:
                    raise FontError(f"No se ha podido encontrar la fuente: {path_to_check}")
    except FileNotFoundError:
        raise FontError("No se ha encontrado el archivo con el listado de fuentes")

def check_images() -> None:
    """
    Comprueba que todas las imagenes listadas en el archivo de recursos existen
    y pueden cargarse correctamente con pygame.

    raises ImageError: Si falta el archivo de listado o alguna imagen.
    """

    try:
        with open("assets/images/images_assets_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                path_to_check = line.strip()
                try:
                    pygame.image.load(f"assets/images/{path_to_check}")
                except FileNotFoundError as error:
                    raise ImageError(f"No se ha podido encontrar la imagen: {path_to_check}")
    except FileNotFoundError:
        raise ImageError("No se ha encontrado el archivo con el listado de imagenes")

def check_sound() -> None:
    """
    Comprueba que todas los audios listadas en el archivo de recursos existen
    y pueden cargarse correctamente con pygame.

    raises MusicError: Si falta el archivo de listado o algún audio.
    """

    try:
        with open("assets/sound/sound_assets_list.txt", "r", encoding="utf-8") as file:
            for line in file:
                path_to_check = line.strip()
                try:
                    pygame.mixer.Sound(f"assets/sound/{path_to_check}")
                except FileNotFoundError as error:
                    raise MusicError(f"No se ha podido encontrar la imagen: {path_to_check}")
    except FileNotFoundError:
        raise MusicError("No se ha encontrado el archivo con el listado de imagenes")

def full_check() -> None:
    """
    Ejecuta la comprobación completa de todos los recursos del juego (fuentes, imágenes y sonidos). Si falta algún recurso, el programa se detiene.
    """
    
    numero_errores = 0
    try:
        check_fonts()
    except FontError as error:
        print(error)
        numero_errores += 1

    try:
        check_images()
    except ImageError as error:
        print(error)
        numero_errores += 2

    try:
        check_sound()
    except MusicError as error:
        print(error)
        numero_errores += 3
    
    if numero_errores == 0:
        print("Ejecutando programa...")
        return
    else:
        print("El programa no se puede ejecutar debido a que no tiene todos recursos debidos")
        fg.terminate()