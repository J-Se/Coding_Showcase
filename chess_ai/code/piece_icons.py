# piece_icons.py
# Author: Remington Ward
# 
# Loads in the piece icons into pygame surfaces

import pygame
import chess
import os

# Load images for white pieces
white_icons = {
    chess.PAWN: pygame.image.load(os.path.join("icons", "white_pawn.png")),
    chess.ROOK: pygame.image.load(os.path.join("icons", "white_rook.png")),
    chess.KNIGHT: pygame.image.load(os.path.join("icons", "white_knight.png")),
    chess.BISHOP: pygame.image.load(os.path.join("icons", "white_bishop.png")),
    chess.QUEEN: pygame.image.load(os.path.join("icons", "white_queen.png")),
    chess.KING: pygame.image.load(os.path.join("icons", "white_king.png"))
}

# Load images for black pieces
black_icons = {
    chess.PAWN: pygame.image.load(os.path.join("icons", "black_pawn.png")),
    chess.ROOK: pygame.image.load(os.path.join("icons", "black_rook.png")),
    chess.KNIGHT: pygame.image.load(os.path.join("icons", "black_knight.png")),
    chess.BISHOP: pygame.image.load(os.path.join("icons", "black_bishop.png")),
    chess.QUEEN: pygame.image.load(os.path.join("icons", "black_queen.png")),
    chess.KING: pygame.image.load(os.path.join("icons", "black_king.png"))
}

# Define a function to get the icon for a given piece type and team
def get_icon(piece_type, team):
    try:
        if team == chess.WHITE:
            return white_icons[piece_type]
        elif team == chess.BLACK:
            return black_icons[piece_type]
        else:
            raise ValueError("Invalid team color")
    except KeyError:
        print("Error: Piece type not found or image file missing.")
        return None