from board import Board


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
		return 'P' if self.color == 'while' else 'p'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos

		directions = -1 if self.color == 'white' else 1
		start_row = 6 if self.color == 'white' else 1

		if board.is_empty(x + directions, y):
			# if we can move there
			moves.append((x + directions, y))
			if x == start_row and board.is_empty(x + 2 * directions, y):
				moves.append((x + 2 * directions, y))


		return moves