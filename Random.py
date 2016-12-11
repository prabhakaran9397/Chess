from chess import ChessBoard
from random import randint

if __name__ == '__main__':
	CBoard = ChessBoard(1, 1)
	CBoard.PrintBoard()
	while CBoard.Move(randint(0,7), randint(0,7), randint(0,7), randint(0,7))==0:
		pass
	CBoard.PrintBoard()