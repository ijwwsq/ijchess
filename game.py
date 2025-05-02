from board import Board

class Game:
  def __init__(self):
    self.board = Board()
    self.turn = 'white'

  def switch_turn(self):
    self.turn = 'black' if self.turn == 'white' else 'white'

  def move(self, from_pos, to_pos):
    x1, y1 = from_pos
    x2, y2 = to_pos

    piece = self.board.get_piece(x1, y1)

    if not piece:
      print("no piece at source pos")
      return False

    if piece.color != self.turn:
      print(f"its {self.turn}'s turn.")
      return False

    legal_moves = piece.get_moves((x1, y1), self.board)

    if (x2, y2) not in legal_moves:
      print("cant do that")
      return False

    target = self.board.get_piece(x2, y2)
    if target:
      print(f"{piece.symbol} captures {target.symbol} at {to_chess_notation(x2, y2)}")

    # move
    self.board.grid[x2][y2] = piece
    self.board.grid[x1][y1] = None

    self.switch_turn()
    return True

  def print_board(self):
    print("  a  b  c  d  e  f  g  h")
    for i in range(7, -1, -1):
      row = self.board.grid[i]
      pieces = '  '.join(p.symbol if p else '.' for p in row)
      print(f"{i + 1} {pieces}")  
