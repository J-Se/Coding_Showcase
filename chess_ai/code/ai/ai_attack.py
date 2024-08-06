# AI that tries to maximize its number of attacking squares

import chess
from pyximport import install; install()
from ai.ai import AI
from ai.ai_basic_material import get_material_difference

def heuristic(board: chess.Board, color: chess.Color) -> float:
    attack_bonus(board, color)
    return get_material_difference(board, color) + attack_bonus(board, color)

def attack_bonus(board: chess.Board, color: chess.Color) -> float:
    sum = 0

    for (square, piece) in board.piece_map().items():
        if piece is not None and piece.color == color:
            # add (number of enemy pieces being attacked by this piece) / 100
            sum += (board.attacks_mask(square) & all_color_pieces_mask(board, not color)).bit_count() / 100
            # add (number of squares being attacked by this piece excluding ally pieces) / 100
            sum += (board.attacks_mask(square) & ~all_color_pieces_mask(board, color)).bit_count() / 100
    
    return sum
    
def all_color_pieces_mask(board: chess.Board, color: chess.Color) -> chess.Bitboard:
    return_board = 0
    for type in chess.PIECE_TYPES:
        return_board |= board.pieces_mask(type, color)
    return return_board

def all_pieces_mask(board: chess.Board) -> chess.Bitboard:
    return all_color_pieces_mask(board, chess.WHITE) | all_color_pieces_mask(board, chess.BLACK)

attack_depth_one = AI(heuristic=heuristic, depth=1)
attack_depth_two = AI(heuristic=heuristic, depth=2)
attack_depth_three = AI(heuristic=heuristic, depth=3)
attack_depth_four = AI(heuristic=heuristic, depth=4)