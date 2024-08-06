# main.py
# Authors: Remington Ward, Jacob Seikel, Eric Lykins
#
# Script for testing the heuristic-based AIs against each other

NUM_DEPTH_ONE_GAMES = 9
NUM_DEPTH_TWO_GAMES = 7
NUM_DEPTH_THREE_GAMES = 5
NUM_DEPTH_FOUR_GAMES = 1

import threading

from chess_game import ChessGame
import ai.ai_random as dumb
import ai.ai_basic_material as normal
import ai.ai_trading as merchant
import ai.ai_aggressive as angy
import ai.ai_attack as edgy
import ai.ai_pawn_pusher as pushy
from pyximport import install; install()
from ai.ai import AI
from chess_game_over import ChessGameOver
from concurrent.futures import ThreadPoolExecutor


WHITE_WON = 0
BLACK_WON = 1
DRAW = 2

all_ais = [dumb, normal, merchant, angy, edgy, pushy]
ai_names = {
    dumb: "Random",
    normal: "Basic",
    merchant: "Trader",
    angy: "Piece pusher",
    edgy: "Attacker",
    pushy: "Pawn pusher",
}

lock = threading.Lock()

def test_ais(num_games: int, depth: int, output_file_path: str):
    """Function to test AI's by playing them against each other."""
    with open(output_file_path, "w") as file:
        file.write(f"TESTING RESULTS DEPTH {depth}\n\n")
    
    print(f"Depth {depth} - Starting tests...")

    file_lock = threading.Lock()
    def run_matchup(white_ai, black_ai):
        nonlocal file_lock
        nonlocal depth
        

        with ThreadPoolExecutor(max_workers=num_games+1) as pool:
            futures = [pool.submit(run_test_game, white_ai, black_ai, depth) for i in range(num_games)]
            results = [future.result() for future in futures]
        
        total = {
            'white_wins' : 0,
            'black_wins' : 0,
            'draws' : 0}
        for result in results:
            for key, value in result.items():
                total[key] += value
        white_wins = total['white_wins']
        black_wins = total['black_wins']
        draws = total['draws']
        
        print(f"Depth {depth} - Finished {ai_names[white_ai]} vs {ai_names[black_ai]}.")
        with file_lock:
            with open(output_file_path, "a") as file:
                file.write(f"White AI is {ai_names[white_ai]} and Black AI is {ai_names[black_ai]}\n")
                file.write(f"White won {white_wins} times, Black won {black_wins} times, and they drew {draws} times.\n")
                file.write("\n\n\n")
    
    for white_ai in all_ais:
        matchup_threads = [threading.Thread(target=run_matchup, args=(white_ai, black_ai)) for black_ai in all_ais]
        for thread in matchup_threads:
            thread.start()
        for thread in matchup_threads:
            thread.join()

    print(f"Depth {depth} - Done \n")
        


def run_test_game(white_ai, black_ai, depth: int) -> int:
    """Runs the game with the given AIs and depth"""
    game = ChessGame(white_ai=AI(heuristic=white_ai.heuristic, depth=depth), black_ai=AI(heuristic=black_ai.heuristic, depth=depth))
    game.set_ai_move_time(0)

    white_wins = 0
    black_wins = 0
    draws = 0

    game_over_data = game.start(display_game=False, print_game=False)
    if game_over_data.game_over_type == ChessGameOver.CHECKMATE:
        if game_over_data.winning_team == ChessGameOver.WHITE:
            result = WHITE_WON
        else:
            result = BLACK_WON
    else:
        result = DRAW

    with lock:
        if result == WHITE_WON:
            white_wins += 1
        elif result == BLACK_WON:
            black_wins += 1
        else:
            draws += 1

    return {
        'white_wins' : white_wins,
        'black_wins' : black_wins,
        'draws' : draws}



# test functions is run here
test_ais(num_games=NUM_DEPTH_ONE_GAMES, depth=1, output_file_path="ai/testing/depth_1_results.txt")
test_ais(num_games=NUM_DEPTH_TWO_GAMES, depth=2, output_file_path="ai/testing/depth_2_results.txt")
test_ais(num_games=NUM_DEPTH_THREE_GAMES, depth=3, output_file_path="ai/testing/depth_3_results.txt")
test_ais(num_games=NUM_DEPTH_FOUR_GAMES, depth=4, output_file_path="ai/testing/depth_4_results.txt")