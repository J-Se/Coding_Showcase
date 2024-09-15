import pygame
import pygame_menu as pm

WIDTH, HEIGHT = 500, 500
LIGHT_GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

def show_menu(screen: pygame.Surface):
    menu = pm.Menu(title="GravSweeper",
                   width=WIDTH,
                   height=HEIGHT)
    
    menu.add.button(title="Play", font_color=BLACK, background_color=LIGHT_GRAY)
    menu.add.label("")
    menu.add.button(title="Settings", font_color=BLACK, background_color=LIGHT_GRAY)

    menu.mainloop(screen)