from chess import ChessBoard
from random import randint

if __name__ == '__main__':
	CBoard = ChessBoard(3, 1)
	CBoard.PrintBoard()
	for i in range(500):
		while CBoard.Move(randint(0,7), randint(0,7), randint(0,7), randint(0,7))==0:
			pass
		CBoard.PrintBoard()