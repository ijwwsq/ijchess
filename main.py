#!env/bin/python
from board import Board
from piece import Piece, Pawn, Queen
from game import Game

board = Board()
#board.grid[6][4] = Pawn('white')

#pawn = board.grid[6][4]
#moves = pawn.get_moves((6, 4), board)

def to_chess_notation(x, y):
  files = 'abcdefgh'
  rank = x+1
  file = files[y]

  return f"{file}{rank}"

game = Game()
game.print_board()
pawn = game.board.get_piece(6, 4)
moves = pawn.get_moves((6, 4), game.board)
print("Legal moves for Pawn at e2:")
for x, y in moves:
  print(to_chess_notation(x, y))
game.move((6, 4), (4, 4))
game.print_board()