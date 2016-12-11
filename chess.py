#!/usr/bin/python
import os

# I need Board 	- X
# I need Pieces 	- X
# I need Players	- X
# I need Rules
# 0 -> Black; 1 -> White

class ChessBoard:
	
	def __init__(self, Height=3, Transition=0.7):
		if Height<1: Height=1
		if Height%2 == 0: Height-=1
		self.Texture 	= "#"
		self.Boxes		= 8
		self.Height		= Height
		self.White		= "\033[97m{}\033[00m" 
		self.Black		= "\033[90m{}\033[00m" 
		self.WhiteP		= "\033[107m\033[90m{}\033[00m"
		self.BlackP		= "\033[100m\033[97m{}\033[00m"
		self.Board 		= []
		self.Transition	= Transition
		self.Message	= ""
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
		self.Set(0, 3, "Q", 0) 						# 4
		self.Set(0, 4, "K", 0) 						# 5
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
		if len(self.Message)>0:
			print self.Message
			self.Message = ""
		print
		sleep(self.Transition)

	def PieceInfo(self, i, j):
		Piece = self.Board[self.index(i)][self.index(j)]; P = []
		Color = {'0' : 0, '7' : 1} # 0 -> Black; 1 -> White
		if Piece[5] == self.Texture:
			P.append(Color[Piece[3]]); P.append(Piece[5])
		else:
			P.append(Color[Piece[4]]); P.append(Piece[11])
		return P

	def Move(self, fi, fj, ti, tj): #from - to
		if self.PieceInfo(fi, fj)[1] == self.Texture:
			return # If its not a piece
		if self.CheckRules(fi, fj, ti, tj):
			Piece = self.Board[self.index(fi)][self.index(fj)]
			if (fi+fj)%2: # Black
				self.Board[self.index(fi)][self.index(fj)] = self.Black.format(self.Texture)
			else: # White
				self.Board[self.index(fi)][self.index(fj)] = self.White.format(self.Texture)
			self.Board[self.index(ti)][self.index(tj)] = Piece

	def CheckRules(self, fi, fj, ti, tj):		# Board Rules
		From = self.PieceInfo(fi, fj)									# From is sure a Piece
		To   = self.PieceInfo(ti, tj)									# To can be a Piece or empty
		Flag = self.IsValid(From, fi, fj, ti, tj)						# Move validity from standard chess rules
		if (To[1]==self.Texture and Flag) or (From[0]!=To[0] and Flag):	# if To is empty or From can kill To
			return True													# Legal
		else:
			return False												# Illegal
	# A fair assumption that the present move in the board is valid, only the next move is validated
	def IsValid(self, Piece, fi, fj, ti, tj):	# Move validation
		if fi==ti and fj==tj:
			self.Message = "WAR: Make a move"
			return 0
		To   = self.PieceInfo(ti, tj)
		if Piece[0]==To[0] and To[1]!=self.Texture:
			self.Message = "ERR: You're betraying"
			return 0
		if   Piece[1] == 'K':					# 'K' => King
			for i in range(-1, 2):
				for j in range(-1, 2):
					if ti==fi+i and tj==fj+j:
						self.Message = "SUC: King moved!"
						return 1
			self.Message = "ERR: King can't make that move"
			return 0
		elif Piece[1] == 'Q':					# 'Q' => Queen
			if fi==ti or fj==tj or abs(fi-ti) == abs(fj-tj):
				self.Message = "SUC: Queen moved!"
				return 1
			self.Message = "ERR: Queen can't make that move"
			return 0
		elif Piece[1] == 'R':					# 'R' => Rook
			if fi==ti or fj==tj:
				self.Message = "SUC: Rook moved!"
				return 1
			self.Message = "ERR: Rook can't make that move"
			return 0
		elif Piece[1] == 'B':					# 'B' => Bishop
			if abs(fi-ti) == abs(fj-tj):
				self.Message = "SUC: Bishop moved!"
				return 1
			self.Message = "ERR: Bishop can't make that move"
			return 0
		elif Piece[1] == 'H':					# 'H' => Knight
			if (abs(fi-ti)==2 and abs(fj-tj)==1) or (abs(fi-ti)==1 and abs(fj-tj)==2):
				self.Message = "SUC: Knight moved!"
				return 1
			self.Message = "ERR: Knight can't make that move"
			return 0
		elif Piece[1] == '6':					# '6' => Pawn
			flag = To[1]!=self.Texture
			if 	 (Piece[0]==0 and
				 (((fi==1 and ti==3) or fi+1==ti) and fj==tj) or 
				 (fi+1==ti and fj-1==tj and flag) or (fi+1==ti and fj+1==tj and flag)):
					self.Message = "SUC: Pawn moved!"
					return 1
			elif (Piece[0]==1 and
				 (((fi==6 and ti==4) or fi-1==ti) and fj==tj) or
				 (fi-1==ti and fj-1==tj and flag) or (fi-1==ti and fj+1==tj and flag)):
					self.Message = "SUC: Pawn moved!"
					return 1
			self.Message = "ERR: Pawn can't make that move"
			return 0 

def clear():
	os.system("clear")

def sleep(i):
	os.system("sleep " + str(i))

if __name__ == '__main__':
	CBoard = ChessBoard(3, 1)
	CBoard.PrintBoard()
	CBoard.Move(1, 3, 3, 3)	# Move the pawn
	CBoard.PrintBoard()
