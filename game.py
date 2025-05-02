from board import Board
from piece import King, Pawn


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

    # castling
    if isinstance(piece, King) and abs(y2 - y1) == 2:
      if y2 == 6:  # kingside
        rook = self.board.get_piece(x1, 7)
        self.board.grid[x1][5] = rook
        self.board.grid[x1][7] = None
      else:  # queenside
        rook = self.board.get_piece(x1, 0)
        self.board.grid[x1][3] = rook
        self.board.grid[x1][0] = None
      if rook:
        rook.has_moved = True
    
    # en passant
    if isinstance(piece, Pawn) and (x2, y2) == self.board.en_passant_target:
      take_x = x1
      self.board.grid[take_x][y2] = None
      print("En passant capture!")
    
    # update en passant possibility
    self.board.en_passant_target = None
    
    if isinstance(piece, Pawn) and abs(x2 - x1) == 2:
      self.board.en_passant_target = ((x1 + x2) // 2, y1)

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
