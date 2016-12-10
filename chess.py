#!/usr/bin/python
import os

#I need Board 	- X
#I need Pieces 	- X
#I need Players	- X
#I need Rules

class ChessBoard:
	
	def __init__(self, Height=3, Transition=0.7):
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
		self.Transition	= Transition
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

	def index(self, i):
		return self.Height*i+(self.Height-1)/2

	def Set(self, i, j, Piece, Color): # 0 -> Black; 1 -> White
		if Color:
			self.Board[self.index(i)][self.index(j)] = self.WhiteP.format(Piece[0])
		else:
			self.Board[self.index(i)][self.index(j)] = self.BlackP.format(Piece[0])

	def ResetBoard(self):
		self.Set(0, 0, "R", 0) 						# 1
		self.Set(0, 1, "B", 0) 						# 2
		self.Set(0, 2, "H", 0) 						# 3
		self.Set(0, 3, "K", 0) 						# 4
		self.Set(0, 4, "Q", 0) 						# 5
		self.Set(0, 5, "H", 0) 						# 6
		self.Set(0, 6, "B", 0) 						# 7
		self.Set(0, 7, "R", 0) 						# 8
		for i in range(8): self.Set(1, i, "6", 0)	# 9 10 11 12 13 14 15 16
		self.Set(7, 0, "R", 1)						#17
		self.Set(7, 1, "B", 1)						#18
		self.Set(7, 2, "H", 1)						#19
		self.Set(7, 3, "Q", 1)						#20
		self.Set(7, 4, "K", 1)						#21
		self.Set(7, 5, "H", 1)						#22
		self.Set(7, 6, "B", 1)						#23
		self.Set(7, 7, "R", 1)						#24
		for i in range(8): self.Set(6, i, "6", 1)	#25 26 27 28 29 30 31 32

	def PrintBoard(self, Space=20):
		clear()
		print
		for Brow in range(self.Boxes*self.Height):
			for Bcol in range(Space):
				print "",
			for Bcol in range(self.Boxes*self.Height):
				print self.Board[Brow][Bcol],
			print
		print
		sleep(self.Transition)

	def Move(self, fi, fj, ti, tj): #from - to
		Piece = self.Board[self.index(fi)][self.index(fj)]
		if (fi+fj)%2: # Black
			self.Board[self.index(fi)][self.index(fj)] = self.Black.format(self.Texture)
		else: # White
			self.Board[self.index(fi)][self.index(fj)] = self.White.format(self.Texture)
		self.Board[self.index(ti)][self.index(tj)] = Piece

def clear():
	os.system("clear")

def sleep(i):
	os.system("sleep " + str(i))

if __name__ == '__main__':
	CBoard = ChessBoard(3, 0.9)
	CBoard.PrintBoard()	# Before Moving
	CBoard.Move(1, 3, 2, 3)
	CBoard.PrintBoard() # After Moving