# main.py
# Authors: Remington Ward, Jacob Seikel, Eric Lykins
#
# The main entry point to the program.
# Handles creating the AIs and the chess game 

import time
import multiprocessing

from chess_game import ChessGame
import ai.ai_random as ai_random
import ai.ai_basic_material as ai_basic_material
import ai.ai_stockfish as ai_stockfish 
import ai.ai_trading as ai_trading 
import ai.ai_aggressive as ai_aggressive 
import ai.ai_attack as ai_attack 

from machine_learning.ai_cnn import ai_cnn

random_ai = ai_random.random_ai
basic_ai = ai_basic_material.material_depth_three
trading_ai = ai_trading.trading_depth_three
aggressive_ai = ai_aggressive.aggressive_depth_three
attacker_ai = ai_attack.attack_depth_three
cnn_ai = ai_cnn()

# -- Set the output style here --
CONSOLE_OUTPUT = False
"""Whether to show console output for the chess game"""

PYGAME_OUTPUT = True
"""Whether to display the game with pygame GUI"""

#  -- Set the AIs here --
# The AIs are:
#  random_ai
#  basic_ai 
#  trading_ai
#  aggressive_ai
#  attacker_ai
#  cnn_ai

WHITE = None
# WHITE = cnn_ai
"""The AI to play white. None for a human player"""

BLACK = basic_ai
# BLACK = random_ai
"""The AI to play black. None for a human player"""


def run_game(game_id=0):
    """Runs the game. Optionally specify an ID"""
    game = ChessGame(white_ai=WHITE, black_ai=BLACK)
    game.set_ai_move_time(0.5)
    
    s = time.time()
    print(f"Playing game {game_id}...")
    game_over_data = game.start(display_game=PYGAME_OUTPUT, print_game=CONSOLE_OUTPUT)
    runtime = time.time() - s
    print(game_over_data)
    print(f'Game ran in {runtime} seconds')
    # In chess a "move" is both players making a move, 
    # so we have half as many moves as the length of the move list
    print(f'Game had {int(len(game.get_past_moves())/2)} moves') 
    return runtime


if __name__ == "__main__":
    run_game()
    # RUN_COUNT = 1
    # print(f"Running {RUN_COUNT} games...")
    # pool_optimized = multiprocessing.Pool(processes=RUN_COUNT)
    # results_optimized = pool_optimized.map(run_game, range(RUN_COUNT))
    # total_time = sum(results_optimized)
    # pool_optimized.close()
    # pool_optimized.join()
    # average =  total_time/RUN_COUNT
    # print("Average time per game:", average)

