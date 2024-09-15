import pygame
from box import Box

LIGHT_GRAY = (150, 150, 150)
PURPLE = (160, 50, 200)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Courier New", 40)

class Tile:
    # x and y refer to the logical coordinates, not the pixel coordinates
    def __init__(self, x: int, y: int, rect: pygame.Rect, is_mine: bool = False):
        self.x = x
        self.y = y
        self.rect = rect
        self.num_adj_mines = 0
        self.box = Box(x, y, self.rect.copy(), is_mine)
        self.text_box = None

    def redraw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, PURPLE, self.rect)
        
        if self.num_adj_mines > 0:
            self.text_box = font.render(str(self.num_adj_mines), False, BLACK)
        else:
            self.text_box = font.render(" ", False, BLACK)

        text_rect = self.text_box.get_rect()
        text_rect.center = self.rect.center # this line centers the text

        screen.blit(self.text_box, text_rect)

    def __str__(self) -> str:
        return f"Tile at ({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return self.__str__()