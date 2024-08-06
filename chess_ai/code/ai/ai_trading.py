# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# AI that prioritizes taking even trades

import chess
from pyximport import install; install()
from ai.ai import AI
from ai.ai_basic_material import get_material_difference

def heuristic(board: chess.Board, color: chess.Color) -> float:
    return get_material_difference(board, color) - (len(board.piece_map().values()) / 100)

trading_depth_two = AI(heuristic=heuristic, depth=2)
trading_depth_one = AI(heuristic=heuristic, depth=1)
trading_depth_three = AI(heuristic=heuristic, depth=3)
trading_depth_four = AI(heuristic=heuristic, depth=4)
trading_depth_five = AI(heuristic=heuristic, depth=5)
trading_depth_six = AI(heuristic=heuristic, depth=6)