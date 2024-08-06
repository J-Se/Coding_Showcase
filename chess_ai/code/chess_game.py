# chess_game.py
#  Author: Remington Ward
#
#  Handles the chess game: 
#   - Taking turns
#   - Main Game loop
#   - keeping track of the past moves
#   - Making calls to the AI


import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from copy import deepcopy

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ai.ai import AI

import chess
from chess_display import ChessDisplay
from chess_game_over import ChessGameOver

class ChessGame:
    """
    Main Chess Game Class
    
    You can initialize with a white_ai and black_ai.

    The AIs are functions that take in the game object and call the move() function on it. 
    """
    def __init__(self, white_ai: "AI" = None, black_ai: "AI" = None):
        self.board = chess.Board()
        self.white_ai = white_ai
        self.black_ai = black_ai
        self.__selected_square = None
        self.__potential_moves = None

    def start(self, display_game=True, print_game=False):
        """
        Start the game. 
        
        This takes control, drawing to the screen and handling input until the game is over.
        """
        self.print_game = print_game
        if display_game:
            self.display = ChessDisplay()
            self.display.draw_board(self)
            pygame.display.flip()
        else:
            if not (self.white_ai and self.black_ai):
                print("[WARNING] no display set for a chess game that has an ai missing")
            self.display = None

        # ai waits for a certain time to make sure it is not moving too fast
        last_ai_move_time = time.time()
        if self.print_game:
            print(self.board)

        # Main game loop
        while True:

            # AI makes a move
            ai_waiting = time.time() - last_ai_move_time < self.min_ai_move_time
            if not ai_waiting:
                if self.board.turn == chess.WHITE and self.white_ai:
                    self.white_ai.ai_move(self.board)
                    last_ai_move_time = time.time()
                elif self.board.turn == chess.BLACK and self.black_ai:
                    self.black_ai.ai_move(self.board)
                    last_ai_move_time = time.time()

            # Game is over
            game_over_data = self.get_game_over()
            if game_over_data:
                if self.display:
                    self.__display_game_over(game_over_data)
                return game_over_data

            if self.display:
                for event in pygame.event.get():
                    # Quit the Game
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        game_over_data = self.get_game_over()
                        if not game_over_data:
                            game_over_data = ChessGameOver()
                            game_over_data.set_game_over_type(ChessGameOver.NOT_OVER)
                        return game_over_data

                    # Player makes a move
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.board.turn == chess.WHITE and not self.white_ai:
                            self.__on_click()
                        elif self.board.turn == chess.BLACK and not self.black_ai:
                            self.__on_click()
            
                # Draw the board
                highlights = None
                if self.__selected_square is not None:
                    moves = self.board.legal_moves
                    highlights = [move.to_square for move in moves if move.from_square == self.__selected_square]
                    if len(highlights) > 0:
                        highlights.append(self.__selected_square)
                    highlights = chess.SquareSet(highlights)
                check = self.board.king(self.board.turn) if self.board.is_check() else None
                self.display.draw_board(self, highlights=highlights, check=check)

    def move(self, move: chess.Move):
        """Make a move"""
        self.board.push(move)
        if self.print_game:
            print(self.board)

    def set_ai_move_time(self, time_in_sec: float):
        """Sets how long to wait before the ai moves"""
        self.min_ai_move_time = time_in_sec

    def get_board(self) -> chess.Board:
        """Get the board"""
        return self.board
    
    def set_board(self, board: chess.Board):
        """Sets a new board position"""
        self.board = board

    def set_team_to_move(self, team):
        """Set whose turn it is"""
        self.board.turn = team

    def get_team_to_move(self) -> str:
        """Gets whose turn it is"""
        return self.board.turn

    def get_past_moves(self) -> list[chess.Move]:
        """
        Gets a list of all the past chess moves, 
        for this purpose a move is just one player's decision, not both
        """
        return self.board.move_stack

    def get_current_moves(self) -> list[chess.Move]:
        """Get a list of all the current legal moves"""
        return self.board.legal_moves

    def get_game_over(self) -> ChessGameOver | None:
        """Get if the game is over"""
        team_to_move = self.board.turn

        if self.board.is_checkmate():
            game_over = ChessGameOver()
            game_over.game_over_type = ChessGameOver.CHECKMATE
            game_over.winning_team = ChessGameOver.WHITE if team_to_move == chess.BLACK else ChessGameOver.BLACK
            return game_over

        if self.board.is_stalemate():
            game_over = ChessGameOver()
            game_over.game_over_type = ChessGameOver.STALEMATE
            game_over.stalemated_team = ChessGameOver.WHITE if team_to_move == chess.WHITE else ChessGameOver.BLACK
            return game_over
        
        if self.board.can_claim_fifty_moves():
            game_over = ChessGameOver()
            game_over.game_over_type = ChessGameOver.FIFTY_MOVE_RULE
            return game_over
        
        return None

    def __on_click(self):
        """The player clicked on the board and it is their turn."""
        mouse_pos = pygame.mouse.get_pos()
        clicked_square = self.display.board_pos(mouse_pos)
        if clicked_square is not None:
            moves = self.board.legal_moves
            if self.__selected_square is None: # No selected piece
                self.__selected_square = clicked_square
                self.__potential_moves = [move for move in moves if move.from_square == self.__selected_square]
            else:
                moves = [m for m in self.__potential_moves if m.to_square == clicked_square]
                if len(moves) > 0: # Clicked a potential move
                    self.move(moves[0])
                    self.__selected_square = None
                    self.__potential_moves = None
                else: # Clicked away from selected piece and moves
                    self.__selected_square = None
                    self.__potential_moves = None
                    self.__on_click()

    def __display_game_over(self, game_over_data: ChessGameOver) -> None:
        """Display that the game is over"""
        self.display.draw_board(self)
        self.display.display_message(game_over_data.message())
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k in ['display']:
                setattr(result, k, v)  # shallow copy for the display
            else:
                setattr(result, k, deepcopy(v, memo))
        return result
        

    