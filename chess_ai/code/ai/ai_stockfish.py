# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# Implementation of Stockfish in our environment

from random import randint
from chess_game import ChessGame
import chess
import chess.engine
from copy import deepcopy
from pyximport import install; install()
from ai.ai import AI
import time
import os.path

def random_heuristic(board: chess.Board, ai_color: str) -> float:
    return 1

random_ai = AI(heuristic=random_heuristic, depth=1)

class Stockfish:
    PATH = "lib\stockfish\stockfish.exe"

    def __init__(self, depth=10):
        if not os.path.isfile(Stockfish.PATH):
            message = "\n" \
                "  Stockfish is not installed.\n" \
                "  Please go download Stockfish at https://stockfishchess.org/download/ \n" \
                "  Extract the files into code/lib/stockfish and rename the executable to stockfish.exe\n"
            raise FileNotFoundError(message)

        self.depth = depth
        self.engine = chess.engine.SimpleEngine.popen_uci(Stockfish.PATH)

    def ai_move(self, board: chess.Board):
        result = self.engine.play(board, chess.engine.Limit(depth=self.depth))
        board.push(result.move)

    def __del__(self):
        try:
            self.engine.quit()
        except:
            pass