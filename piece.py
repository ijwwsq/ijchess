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
		directions = [
			(1, 1), 
			(-1, 1), 
			(1, -1), 
			(-1, -1), 
			(0, 1), 
			(0, -1), 
			(1, 0), 
			(-1, 0)
		]
		moves = []
		x, y = pos
		capture = 0 # add point for piece here in future

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
					break # cant move further if we capture the figure
				else:
					break

				i+= 1

		return moves

class King(Piece):
	@property
	def symbol(self):
		return 'K' if self.color == 'white' else 'k'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos

		directions = [
			(1, 0), (-1, 0),  # vertical
			(0, 1), (0, -1),  # horizontal
			(1, 1), (1, -1),  # diagonals
			(-1, 1), (-1, -1)
		]

		for dx, dy in directions:
			new_x, new_y = x + dx, y + dy

			if not board.on_board(new_x, new_y):
				continue

			target = board.get_piece(new_x, new_y)

			# todo: capture logic here
			if target is None or target.color != self.color:
				moves.append((new_x, new_y))

		return moves

class Rook(Piece):
	@property
	def symbol(self):
		return 'R' if self.color == 'white' else 'r'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		
		for dx, dy in directions:
			i = 1
		
			while True:
				new_x, new_y = x + dx * i, y + dy * i
				if not board.on_board(new_x, new_y):
					break
		
				if board.is_empty(new_x, new_y):
					moves.append((new_x, new_y))
				elif board.get_piece(new_x, new_y).color != self.color:
					moves.append((new_x, new_y))
					break
				else:
					break
				i += 1
		
		return moves

class Bishop(Piece):
	@property
	def symbol(self):
		return 'B' if self.color == 'white' else 'b'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos
		directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
		for dx, dy in directions:
			i = 1
			
			while True:
				new_x, new_y = x + dx * i, y + dy * i
				if not board.on_board(new_x, new_y):
					break
			
				if board.is_empty(new_x, new_y):
					moves.append((new_x, new_y))
				elif board.get_piece(new_x, new_y).color != self.color:
					moves.append((new_x, new_y))
					break
				else:
					break
				i += 1
		
		return moves

class Knight(Piece):
	@property
	def symbol(self):
		return 'N' if self.color == 'white' else 'n'

	def get_moves(self, pos, board):
		moves = []
		x, y = pos
		jumps = [(2, 1), (1, 2), (-1, 2), (-2, 1),
							(-2, -1), (-1, -2), (1, -2), (2, -1)]

		for dx, dy in jumps:
			new_x, new_y = x + dx, y + dy
			if not board.on_board(new_x, new_y):
				continue
			target = board.get_piece(new_x, new_y)
			if target is None or target.color != self.color:
				moves.append((new_x, new_y))

		return moves
