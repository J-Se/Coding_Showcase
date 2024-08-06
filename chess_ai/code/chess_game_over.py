# chess_game_over.py
#  Author: Remington Ward
#
#  Describes the data that describes how a chess game ended.


class ChessGameOver:
    """Class for holding information about how a chess game ended"""

    CHECKMATE = "Checkmate"
    STALEMATE = "Stalemate"
    RESIGNATION = "Resignation"
    NOT_OVER = "Game not over"
    FIFTY_MOVE_RULE = "Fifty move rule"
    INSUFFICIENT_MATERIAL = "Insufficient checkmating material"

    WHITE = "White"
    BLACK = "Black"
    
    game_over_type = NOT_OVER
    winning_team = None
    stalemated_team = None

    def set_game_over_type(self, game_over_type):
        """What ended the game"""
        self.game_over_type = game_over_type

    def message(self) -> str:
        """The message to display for this game over"""
        return self.game_over_type
    
    def __str__(self) -> str:
        if self.winning_team is not None:
            return f'{self.game_over_type}! \n{self.winning_team} won.'
        elif self.stalemated_team is not None:
            return f'{self.game_over_type}! \n{self.stalemated_team} was stalemated.'
        else:
            return f'{self.game_over_type}!'