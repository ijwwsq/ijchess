from piece import Pawn, Queen

class Board():
	def __init__(self):
		self.grid = self.setup_board()
		self.turn = 'white'
			
	def setup_board(self):
		board = [[None]*8 for _ in range(8)]
		board[1] = [Pawn('white') for _ in range(8)]
		board[6] = [Pawn('black') for _ in range(8)]

		board[0][3] = Queen('white')
		board[7][3] = Queen('black')
		return board

	def move_piece(self, from_pos, to_pos):
		pass
		# if legal -> go (from_pos -> to_pos)

	def on_board(self, x, y):
		return 0 <= x < 8 and 0 <= y < 8

	def is_empty(self, x, y):
		return self.on_board(x, y) and self.grid[x][y] is None

	def get_piece(self, x, y):
		if self.on_board(x, y):
			return self.grid[x][y]
		return None
