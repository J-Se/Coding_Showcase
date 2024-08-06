# cython: language_level=3

# Chess AI Project
# Eric Lykins, Jacob Seikel, and Remington Ward
# General AI Class

from random import randint
from typing import Callable
from chess_game import ChessGame
cimport chess
from copy import deepcopy
cimport cython
import concurrent.futures

cdef bint parallelization = False
cdef bint caching = False
cdef bint printing = True

ctypedef float (*h_type)(chess.Board, chess.Color)

"""
General class for an AI
Requires a heuristic function and a depth value for instantiation
Contains a function (ai_move) which selects and makes a move on a board
"""
cdef class AI:
    cdef int depth
    cdef object heuristic
    cdef dict memo

    def __init__(self, object heuristic, int depth):
        self.heuristic = heuristic # a heuristic should take a game state and the color from which it bases its perspective
        self.depth = depth if depth >= 1 else 1
        if caching:
            self.memo = {}


    @cython.boundscheck(False)
    @cython.wraparound(False)
    def ai_move(self, board):
        cdef float max
        cdef list legal_moves
        cdef list move_values
        cdef list potential_moves
        cdef int random_int
        # def chess.Move selected_move

        legal_moves = list(board.legal_moves)
        potential_moves = []

        if parallelization:
            def eval_move(move):
                return self.__eval_move(move, board.copy())

            with concurrent.futures.ThreadPoolExecutor(max_workers=60) as executor:
                move_values = list(executor.map(eval_move, board.legal_moves))


            max = float("-inf")
            potential_moves = []
            for move, value in zip(board.legal_moves, move_values):
                if printing:
                    print(move, "has value", round(value, 2))

                if value >= max - 0.0001:
                    if value > max + 0.0001:
                        potential_moves.clear()
                        max = value
                    potential_moves.append(move)

        else:
            max = float("-inf")
            for move in list(board.legal_moves):
                value = self.__eval_move(move, board)
                if printing:
                    print(move, "has value", round(value, 2))

                if value >= max - 0.0001:
                    if value > max + 0.0001:
                        potential_moves.clear()
                        max = value
                    potential_moves.append(move)


        if len(potential_moves) == 0:
            return

        if printing:
            print("\n")
            for move in potential_moves:
                print(f"{move} is a potential move")

        random_int = randint(0, len(potential_moves) - 1)
        selected_move = potential_moves[random_int]

        if printing:
            print(f"\n{selected_move} was selected\n\n")

        board.push(selected_move)


    @cython.boundscheck(False)
    @cython.wraparound(False)
    def __eval_move(self, move, board) -> float:
        board.push(move)
        move_value = self.__minimax(board, not board.turn, self.depth - 1)
        board.pop()
        return move_value


    @cython.boundscheck(False)
    @cython.wraparound(False)
    def __minimax(self, board, bint ai_color, int curr_depth, float alpha = float("-inf"), float beta = float("inf")) -> float:
        cdef list moves
        #def chess.Color color_to_move
        cdef float best_val
        cdef float move_val
        cdef int board_hash

        if caching:
            board_hash = hash(board.fen() + str(board.turn == ai_color))
            if board_hash in self.memo:
                return self.memo[board_hash]
        
        if curr_depth == 0:
            return self.heuristic(board, ai_color)

        moves = list(board.legal_moves)
        color_to_move = board.turn

        if ai_color == color_to_move:
            best_val = float("-inf")

            if board.is_checkmate():
                return -10000 - curr_depth

            if board.is_stalemate():
                return -5

            for move in moves:
                board.push(move)
                move_val = self.__minimax(board, ai_color, curr_depth - 1, alpha, beta)
                board.pop()

                best_val = max(best_val, move_val)
                alpha = max(alpha, best_val)

                if beta <= alpha:
                    break
            
            if caching:
                self.memo[board_hash] = best_val
            return best_val
        
        else:
            best_val = float("inf")

            if board.is_checkmate():
                return 10000 + curr_depth

            if board.is_stalemate():
                return 5

            for move in moves:
                board.push(move)
                move_val = self.__minimax(board, ai_color, curr_depth - 1, alpha, beta)
                board.pop()

                best_val = min(best_val, move_val)
                beta = min(beta, best_val)

                if beta <= alpha:
                    break
            
            if caching:
                self.memo[board_hash] = best_val
            return best_val