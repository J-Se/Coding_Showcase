import pygame

pygame.init()
pygame.font.init() # this must be done before Tile is imported

from grid import Grid
from main_menu import show_menu

NUM_COLUMNS = 10
NUM_ROWS = 10
WINDOW_SIZE_PIXELS = 500
SCREEN = pygame.display.set_mode((WINDOW_SIZE_PIXELS, WINDOW_SIZE_PIXELS))

grid = Grid(NUM_COLUMNS, NUM_ROWS, SCREEN)
tiles = grid.tiles

# show_menu(SCREEN)

game_is_running = True

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_is_running = False
            break

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_tiles = [tile for tile_row in tiles for tile in tile_row if tile.rect.collidepoint(pos)]

            if len(clicked_tiles) > 0:
                for tile in clicked_tiles:
                    grid.update_grid(tile)
                    grid.update_num_adj_mines()
                    # print(f"{tile} now has {tile.num_adj_mines} adjacent mines")
                
                grid.update_display(SCREEN)
    
    if not game_is_running:
        break

'''
def main():
    SCREEN.fill(LIGHT_GRAY)
    draw_grid()

    pygame.display.update()

    while True:
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.MOUSEBUTTONUP:

                pos = pygame.mouse.get_pos()
                clicked_tiles = [tile for tile_row in tiles for tile in tile_row if tile.rect.collidepoint(pos)]

                if len(clicked_tiles) > 0:
                    for tile in clicked_tiles:
                        print(f"({tile.x}, {tile.y}) was clicked")


def draw_grid(block_size: int = int(WINDOW_SIZE / 10), mine_chance: float = 0.1):
    print(f"block size = {block_size}")

    global tiles

    logical_y = 0
    for y in range((WINDOW_SIZE - block_size), -block_size, -block_size):
        tile_row = []
        logical_x = 0

        for x in range(0, WINDOW_SIZE, block_size):
            is_mine = random.random() < mine_chance
            rect = pygame.Rect(x, y, block_size, block_size)
            tile = Tile(logical_x, logical_y, rect, is_mine)
            color = RED if is_mine else DARK_GRAY

            pygame.draw.rect(SCREEN, color, rect)
            tile_row.append(tile)
            logical_x = logical_x + 1

        tiles.append(tile_row)
        logical_y = logical_y + 1
        
main()
'''