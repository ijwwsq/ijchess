#!env/bin/python
from board import Board
from piece import Piece, Pawn, Queen

board = Board()
#board.grid[6][4] = Pawn('white')

#pawn = board.grid[6][4]
#moves = pawn.get_moves((6, 4), board)

def to_chess_notation(x, y):
  files = 'abcdefgh'
  rank = x+1
  file = files[y]

  return f"{file}{rank}"

board.grid[4][5] = Queen('white')
queen = board.grid[4][5]
moves = queen.get_moves((4, 5), board)


print("  a  b  c  d  e  f  g  h")
for i in range(7, -1, -1):
    rank = i + 1
    row = board.grid[i]
    row_str = '  '.join(piece.symbol if piece else '.' for piece in row)
    print(f"{rank} {row_str}")

# queen = board.grid[0][3]
# moves = queen.get_moves((0, 3), board)
for i in moves:
  print(to_chess_notation(i[0], i[1]), end=', ')
print()
