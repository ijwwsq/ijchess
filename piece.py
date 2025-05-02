class Piece:
	def __init__(self, color):
		self.color = color
	
	@property
	def symbol(self):
		raise NotImplementedError('each piec emust define its own symbol')

	def get_moves(sel, pos, board):
		raise NotImplementedError('each piece must implements its own logic')

class Pawn(Piece):
	@property
	def symbol(self):
		return 'P' if self.color == 'white' else 'p'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos

		# moves by 1, but can do 2 if its on the start row
		directions = -1 if self.color == 'white' else 1
		start_row = 6 if self.color == 'white' else 1

		if board.is_empty(x + directions, y):
			moves.append((x + directions, y))
			if x == start_row and board.is_empty(x + 2 * directions, y):
				moves.append((x + 2 * directions, y))


		return moves

class Queen(Piece):
	@property
	def symbol(self):
		return 'Q' if self.color == 'white' else 'q'

	def get_moves(self, pos, board):
		pass	
		# moves in every direction by 1
		directions = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
		moves = []
		x, y = pos

		for dx, dy in directions:
			i = 1

			while True:
				new_x, new_y = x + dx*i, y + dy*i
				
				if not board.on_board(new_x, new_y):
					break
				
				if board.is_empty(new_x, new_y):
					moves.append((new_x, new_y))
				elif board.get_piece(new_x, new_y).color != self.color:
					moves.append((new_x, new_y)) # capture
					print(f'capture on {new_x} {new_y}')
					break # cant move after the capture
				else:
					break

				i+= 1

		return moves

class King(Piece): pass
class Rook(Piece): pass
class Bishop(Piece): pass
class Knight(Piece): pass