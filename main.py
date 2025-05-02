#!env/bin/python
from board import Board
from piece import Piece, Pawn, Queen
from game import Game

# board = Board()
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
notation_moves = ', '.join(to_chess_notation(x, y) for x, y in moves)
print(f"Legal moves for Pawn at e7: {notation_moves}")

print("going e7 -> e5")
game.move((6, 4), (4, 4))
game.print_board()

game.board.grid[4][3] = Pawn('white')

white_pawn = game.board.get_piece(4, 3)
moves = white_pawn.get_moves((4, 3), game.board)
notation_moves = ', '.join(to_chess_notation(x, y) for x, y in moves)
print(f"Legal moves for White Pawn at d5: {notation_moves}")

print("white plays d5 -> e6 (en passant)")
game.move((4, 3), (5, 4))
game.print_board()