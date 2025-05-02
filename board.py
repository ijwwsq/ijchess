class Board():
	def __init__(self):
		self.grid = self.setup_board()
		self.turn = 'white'
			
	def setup_board(self):
		board = [[None]*8 for _ in range(8)]
		return board

	def move_piece(self, from_pos, to_pos):
		pass
		# if legal -> go (from_pos -> to_pos)

	def on_board(self, x, y):
		return 0 <= x < 8 and 0 <= y < 8

	def is_empty(self, x, y):
		return self.on_board(x, y) and self.grid[x][y] is None
