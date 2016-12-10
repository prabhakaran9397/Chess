#!/usr/bin/python
	
#I need Board
#I need Pieces
#I need Players
#I need Rules

class ChessBoard:
	
	def __init__(self, Height=3):
		if Height<1: Height=1
		if Height%2 == 0: Height-=1
		self.Texture 	= "#"
		self.Boxes		= 8
		self.Height		= Height
		self.White		= "\033[98m{}\033[00m" # Bash Black
		self.Black		= "\033[91m{}\033[00m" # Bash Red
		self.Board 		= []
		for Brow in range(self.Boxes*self.Height):
			Row = []
			for Bcol in range(self.Boxes*self.Height):
				if (Brow/self.Height)%2 == 0:
					if (Bcol/self.Height)%2 == 0:
						Row.append(self.White.format(self.Texture))
					else:
						Row.append(self.Black.format(self.Texture))
				else: 
					if (Bcol/self.Height)%2 == 0:
						Row.append(self.Black.format(self.Texture))
					else:
						Row.append(self.White.format(self.Texture))
			self.Board.append(Row)

	def set(self, i, j, Piece, Color):
		# 0 -> Black; 1 -> White
		if Color:
			self.Board[self.Height*i+(self.Height-1)/2][self.Height*j+(self.Height-1)/2] = \
			self.White.format(Piece[0])
		else:
			self.Board[self.Height*i+(self.Height-1)/2][self.Height*j+(self.Height-1)/2] = \
			self.Black.format(Piece[0])

	def PrintBoard(self, Space=20):
		print
		for Brow in range(self.Boxes*self.Height):
			for Bcol in range(Space):
				print "",
			for Bcol in range(self.Boxes*self.Height):
				print self.Board[Brow][Bcol],
			print
		print

if __name__ == '__main__':
	CBoard = ChessBoard(3)
	CBoard.set(0, 3, "K", 1)
	CBoard.PrintBoard()
