import pygame

LIGHT_GRAY = (150, 150, 150)
RED = (255, 0, 0)

class Box:
    # x and y refer to the logical coordinates, not the pixel coordinates
    def __init__(self, x: int, y: int, rect: pygame.Rect, is_mine: bool = False):
        self.curr_x = x
        self.curr_y = y
        self.rect = rect
        self.is_mine = is_mine
        self.curr_speed = 0 # positive speed = going down

    def redraw(self, screen: pygame.Surface):
        if self.rect is not None:
            pygame.draw.rect(screen, RED if self.is_mine else LIGHT_GRAY, self.rect)