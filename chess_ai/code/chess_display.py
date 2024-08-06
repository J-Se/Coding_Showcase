# chess_display.py
#  Author: Remington Ward
#
#  Displays the board for a chess game. 
#  Also handles getting the chess square from the mouse position

import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from chess_game import ChessGame

from piece_icons import get_icon
import chess

def _get_square(row:int, col:int) -> chess.Square:
    """Get the chess square from row and col 0-7"""
    rank_values = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h"
    }
    square_name = f"{rank_values[col]}{8 - row}"
    return chess.parse_square(square_name)

class ChessDisplay:
    """Class for displaying the chess board"""

    def __init__(self):
        # WINDOW SIZE
        self.WINDOW_WIDTH = 700
        self.WINDOW_HEIGHT = 700
        self.BOARDER_WIDTH = 20
        self.BOARDER_HEIGHT = 20

        # COLORS
        self.BOARDER_COLOR = (92, 65, 35)
        self.WHITE_SPACE = (242, 240, 211)
        self.BLACK_SPACE = (199, 165, 127)
        self.SELECTED_COLOR = (255, 255, 0)
        self.HIGHLIGHT_WHITE_SPACE = (230, 230, 120)
        self.HIGHLIGHT_BLACK_SPACE = (200, 200, 0)
        self.CHECK_COLOR = (230, 100, 100)

        # Calculate board size
        self.BOARD_TOP_LEFT = (self.BOARDER_WIDTH, self.BOARDER_HEIGHT)
        self.BOARD_BOT_RIGHT = (self.WINDOW_WIDTH-self.BOARDER_WIDTH, 
                                self.WINDOW_HEIGHT-self.BOARDER_HEIGHT)
        self.BOARD_WIDTH = self.BOARD_BOT_RIGHT[0] - self.BOARD_TOP_LEFT[0]
        self.BOARD_HEIGHT = self.BOARD_BOT_RIGHT[1] - self.BOARD_TOP_LEFT[1]
        self.SQUARE_WIDTH = self.BOARD_WIDTH / 8
        self.SQUARE_HEIGHT = self.BOARD_HEIGHT / 8

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Chess Game")

    # Get the board position given the mouse position
    def board_pos(self, mouse_pos: tuple[int,int]) -> chess.Square | None:
        """Get the board position for the current mouse position"""
        clicked_row = int((mouse_pos[1] - self.BOARD_TOP_LEFT[0]) // self.SQUARE_WIDTH)
        clicked_col = int((mouse_pos[0] - self.BOARD_TOP_LEFT[1]) // self.SQUARE_HEIGHT)
        if clicked_row < 0 or clicked_row > 7 or clicked_col < 0 or clicked_col > 7:
            return
        return _get_square(clicked_row, clicked_col)

    def display_message(self, message):
        """Display a message"""
        font_size = int(self.WINDOW_WIDTH / 12)
        font = pygame.font.Font(None, font_size)
        text = font.render(message, True, (230, 230, 230), (30, 30, 30))
        message_size = font.size(message)
        pos = (
            self.WINDOW_WIDTH / 2 - message_size[0] / 2, 
            self.WINDOW_HEIGHT / 3 - message_size[1] / 2
        )
        self.screen.blit(text, pos)

    # Function to draw the chessboard
    def draw_board(self, game: "ChessGame", 
                   highlights: chess.SquareSet=None, 
                   check :chess.Square=None):
        """Draw the given chess board to the screen"""
        if highlights is None:
            highlights = chess.SquareSet()

        self.SQUARE_WIDTH = self.BOARD_WIDTH / 8
        self.SQUARE_HEIGHT = self.BOARD_HEIGHT / 8

        # Draw boarder and background
        pygame.draw.rect(self.screen, self.BOARDER_COLOR, 
                        (0, 0, self.WINDOW_HEIGHT, self.WINDOW_WIDTH))
        pygame.draw.rect(self.screen, self.WHITE_SPACE, 
                        (self.BOARD_TOP_LEFT[0], self.BOARD_TOP_LEFT[1], self.BOARD_WIDTH, self.BOARD_HEIGHT))

        for row in range(8):
            for col in range(8):
                square = _get_square(row, col)

                # Draw the square
                if (row + col) % 2 == 0:
                    color = self.WHITE_SPACE
                    if square in highlights: 
                        color = self.HIGHLIGHT_WHITE_SPACE
                else:
                    color = self.BLACK_SPACE
                    if square in highlights: 
                        color = self.HIGHLIGHT_BLACK_SPACE
                if check is not None and square == check:
                    color = self.CHECK_COLOR
                rect = (self.BOARD_TOP_LEFT[0] + (col * self.SQUARE_HEIGHT),
                        self.BOARD_TOP_LEFT[1] + (row * self.SQUARE_WIDTH), 
                        self.SQUARE_HEIGHT, self.SQUARE_WIDTH)
                pygame.draw.rect(self.screen, color, rect)

                # Draw the piece at the current position
                piece = game.board.piece_at(square)
                if piece is not None:
                    icon = get_icon(piece.piece_type, piece.color)
                    icon = pygame.transform.scale(icon, (self.SQUARE_WIDTH, self.SQUARE_HEIGHT))
                    self.screen.blit(icon, rect)
        pygame.display.flip()
