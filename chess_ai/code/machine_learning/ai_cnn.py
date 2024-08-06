# ai_machine_learning.py
#  Author: Remington Ward
#
#  This file utilizes a convolutional nueral network trained in the machine_learning/cnn_training.ipynb file.
#  The nueral network ranks all the possible moves and this AI simply chooses the highest ranked legal move.

import chess
import torch
import numpy as np  
import random
import numpy as np
from bidict import bidict

# Required import so that torch can load the CNN
from machine_learning.cnn import CNN

moves_indexer = bidict({
    f"{chess.square_name(s1)}{chess.square_name(s2)}" : s1*100+s2 for s1 in chess.SQUARES for s2 in chess.SQUARES
})

def board_to_array(board):
    # Create an 8x8 array where each cell contains a unique value for each piece type and color
    piece_values = {
        'P': 1, 'N': 2, 'B': 3, 'R': 4, 'Q': 5, 'K': 6,  # White pieces
        'p': 7, 'n': 8, 'b': 9, 'r': 10, 'q': 11, 'k': 12 # Black pieces
    }
    # Initialize an empty board with zeros
    array = np.zeros((8, 8))
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i, j))
            if piece:
                array[i, j] = piece_values.get(piece.symbol(), 0)
    return array


class ai_cnn:
    def __init__(self):
        self.model = torch.load('machine_learning/saved_models/model_1.pth')
        self.model.eval()  # Set the model to evaluation mode

        # If using a GPU
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)

    def get_legal_move(self, board: chess.Board):
        model = self.model
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # Assuming board_state is preprocessed correctly for the model input
        board_state = board_to_array(board)  # Define your preprocessing function
        board_state = torch.tensor(board_state).float().unsqueeze(0).to(device)
        model.eval()
        with torch.no_grad():
            # Get model output
            output = model(board_state)
            
            # Get indices of the moves sorted by confidence (highest first)
            probabilities, indices = torch.sort(output, descending=True)
            
            # Check each move for legality
            for idx in indices[0]:  # Assuming the model outputs move indices directly
                move_code = idx.item()
                if move_code in moves_indexer.inverse:  # Check if move_code is a valid key
                    move_str = moves_indexer.inverse[move_code]  # Convert index back to move
                    start = move_str[0:2]
                    end = move_str[2:4]
                    for move in board.legal_moves:
                        if chess.square_name(move.from_square) == start and  chess.square_name(move.from_square) == end:
                            move.promotion = chess.QUEEN if move.promotion is not None else None
                            return move
        return None 

    def ai_move(self, board: chess.Board):
        move = self.get_legal_move(board)
        if move is not None:
            board.push(move)
            return
        print("machine Learning ai did not generate a legal move")
        moves = list(board.legal_moves)
        board.push(random.randint(0,len(moves)-1))

