import pygame
from pygame import locals

# def loadImage(pathFromSelf:str) -> pygame.Surface:
#     """Uses pygame to load an image. Path is expected to start from the Strobe/ folder."""
#     return pygame.image.load(__file__.replace("mod.py", pathFromSelf))

def zoomImage(image:pygame.Surface, size:tuple) -> pygame.Surface:
    """Scale a pygame image by a selected amount. Automatically uses 2x if possible."""
    if size == (2, 2):
        return pygame.transform.scale2x(image)
    else:
        return pygame.transform.scale(image, size)

def kill():
    return None