# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# AI that makes random moves (unless it sees checkmate)

from random import randint
from chess_game import ChessGame
import chess
from copy import deepcopy
from pyximport import install; install()
from ai.ai import AI
import time

def heuristic(board: chess.Board, ai_color: str) -> float:
    return 1

random_ai = AI(heuristic=heuristic, depth=1)