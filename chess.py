#!/usr/bin/python
	
#I need Board - X
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
		self.White		= "\033[97m{}\033[00m" 
		self.Black		= "\033[90m{}\033[00m" 
		self.WhiteP		= "\033[107m{}\033[00m"
		self.BlackP		= "\033[100m{}\033[00m"
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
		self.ResetBoard()

	def Set(self, i, j, Piece, Color):
		# 0 -> Black; 1 -> White
		if Color:
			self.Board[self.Height*i+(self.Height-1)/2][self.Height*j+(self.Height-1)/2] = \
			self.WhiteP.format(Piece[0])
		else:
			self.Board[self.Height*i+(self.Height-1)/2][self.Height*j+(self.Height-1)/2] = \
			self.BlackP.format(Piece[0])

	def ResetBoard(self):
		self.Set(0, 0, "R", 0)
		self.Set(0, 1, "B", 0)
		self.Set(0, 2, "H", 0)
		self.Set(0, 3, "K", 0)
		self.Set(0, 4, "Q", 0)
		self.Set(0, 5, "H", 0)
		self.Set(0, 6, "B", 0)
		self.Set(0, 7, "R", 0)
		for i in range(8):
			self.Set(1, i, "6", 0)
		self.Set(7, 0, "R", 1)
		self.Set(7, 1, "B", 1)
		self.Set(7, 2, "H", 1)
		self.Set(7, 3, "Q", 1)
		self.Set(7, 4, "K", 1)
		self.Set(7, 5, "H", 1)
		self.Set(7, 6, "B", 1)
		self.Set(7, 7, "R", 1)
		for i in range(8):
			self.Set(6, i, "6", 1)

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
	CBoard.PrintBoard()
