from board import Board
from piece import Piece, Pawn

board = Board()
board.grid[6][4] = Pawn('white')

pawn = board.grid[6][4]
moves = pawn.get_moves((6, 4), board)

print(moves)
