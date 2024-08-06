# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# AI that tries to push all of its pieces forward

import chess
from pyximport import install; install()
from ai.ai import AI
from ai.ai_basic_material import get_material_difference

def heuristic(board: chess.Board, color: chess.Color) -> float:
    material_difference = get_material_difference(board, color)
    return material_difference + push_bonus(board, color)

def push_bonus(board: chess.Board, color: chess.Color) -> float:
    white_sum = 0
    black_sum = 0
    for (square, piece) in board.piece_map().items():
        if piece is not None:
            if piece.color == chess.WHITE:
                white_sum += chess.square_rank(square) / 100.0
            else:
                black_sum += (7 - chess.square_rank(square)) / 100.0

    if color == chess.WHITE:
        return white_sum - black_sum
    else:
        return black_sum - white_sum


def get_rank(square: chess.Square) -> int:
    """returns rank from 0 to 7"""
    return int(square / 8)

aggressive_depth_one = AI(heuristic=heuristic, depth=1)
aggressive_depth_two = AI(heuristic=heuristic, depth=2)
aggressive_depth_three = AI(heuristic=heuristic, depth=3)
aggressive_depth_four = AI(heuristic=heuristic, depth=4)