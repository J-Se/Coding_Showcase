import pygame
from tile import Tile
from random import random

TILE_SIZE = 50
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (50, 50, 50)
RED = (255, 0, 0)

TILE_GAP = 4
MINE_CHANCE = 0.1

class Grid:
    def __init__(self, width: int, height: int, screen: pygame.Surface):
        screen.fill(DARK_GRAY)

        self.width = width
        self.height = height

        self.tiles: list[list[Tile]] = [] # list of rows

        for y in range(0, height):
            tile_row = []

            for x in range(0, width):
                new_rect = pygame.Rect(x * TILE_SIZE + TILE_GAP / 2, y * TILE_SIZE + TILE_GAP / 2, TILE_SIZE - TILE_GAP, TILE_SIZE - TILE_GAP)
                new_tile = Tile(x, y, new_rect, random() < MINE_CHANCE)
                tile_row.append(new_tile)

            self.tiles.append(tile_row)
        
        self.update_display(screen)
    
    def update_display(self, screen: pygame.Surface): # redraw all rects
        for tile_row in self.tiles:
            for tile in tile_row:
                tile.redraw(screen)
                if tile.box is not None:
                    tile.box.redraw(screen)

        pygame.display.update()

    # this function updates the grid given the tile clicked
    def update_grid(self, tile_clicked: Tile):
        if tile_clicked.box is None:
            return
        
        if tile_clicked.box.is_mine: # TODO: put the losing logic here
            return
        
        tile_clicked.box = None
        # print(f"deleted box at {tile_clicked}")
        
        def next_highest_box(column: list[Tile], curr_index: int) -> Tile:
            # print(f"current index is {curr_index}")
            # print(f"checked boxes are {list(reversed(column[:curr_index]))}")
            for tile in reversed(column[:curr_index]):
                if tile.box is not None:
                    # print(f"next highest box was {tile}")
                    return tile
                
            return None

        tile_columns = list(zip(*self.tiles))
        tile_columns = [list(col) for col in tile_columns]

        for column in tile_columns:
            for tile in reversed(column):
                if tile.box is None:
                    next_highest_box_tile = next_highest_box(column, tile.y)
                    if next_highest_box_tile is not None:
                        next_highest_box_tile.box.rect = tile.rect
                        tile.box = next_highest_box_tile.box
                        next_highest_box_tile.box = None
    
    def update_num_adj_mines(self):
        for tile_row in self.tiles:
            for tile in tile_row:
                adj_tiles = self.get_adj_tiles(tile)
                tile.num_adj_mines = sum([1 for adj_tile in adj_tiles if adj_tile.box is not None and adj_tile.box.is_mine])
        
    def get_adj_tiles(self, tile: Tile) -> list[Tile]:
        adj_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # y, then x

        if tile.y == 0:
            adj_offsets.remove((-1, -1))
            adj_offsets.remove((-1, 0))
            adj_offsets.remove((-1, 1))

        if tile.y == self.height - 1:
            adj_offsets.remove((1, -1))
            adj_offsets.remove((1, 0))
            adj_offsets.remove((1, 1))

        if tile.x == 0:
            adj_offsets.remove((0, -1))
            if adj_offsets.__contains__((-1, -1)):
                adj_offsets.remove((-1, -1))
            if adj_offsets.__contains__((1, -1)):
                adj_offsets.remove((1, -1))
        
        if tile.x == self.height - 1:
            adj_offsets.remove((0, 1))
            if adj_offsets.__contains__((-1, 1)):
                adj_offsets.remove((-1, 1))
            if adj_offsets.__contains__((1, 1)):
                adj_offsets.remove((1, 1))

        return [self.tiles[tile.y + offset[0]][tile.x + offset[1]] for offset in adj_offsets]