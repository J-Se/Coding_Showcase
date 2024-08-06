# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# basic AI that tries to capture and protect material

import chess
from pyximport import install; install()
from ai.ai import AI

def heuristic(board: chess.Board, team: chess.Color) -> float:
    return get_material_difference(board, team)

def get_material_difference(board: chess.Board, team: chess.Color) -> float:
    """Get material difference after a move, positive if given team has more material"""
    return get_material_count(board, team) - get_material_count(board, not team)


def get_material_count(board: chess.Board, team: chess.Color) -> float:
    """Get material count of a team"""
    piece_values = {
        chess.PAWN: 1,
        chess.BISHOP: 3,
        chess.KNIGHT: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    return sum([piece_values[piece.piece_type] for piece in board.piece_map().values() if piece is not None and piece.color==team])

material_depth_one = AI(heuristic=get_material_difference, depth=1)
material_depth_two = AI(heuristic=get_material_difference, depth=2)
material_depth_three = AI(heuristic=get_material_difference, depth=3)
material_depth_four = AI(heuristic=get_material_difference, depth=4)
material_depth_five = AI(heuristic=get_material_difference, depth=5)
material_depth_six = AI(heuristic=get_material_difference, depth=6)