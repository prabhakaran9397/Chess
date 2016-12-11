from chess import ChessBoard
from random import randint
from player import Player

# Play1 is random
def Play1():
	status=0
	while status==0:
		status = CBoard.Move(randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7), 1)
	CBoard.PrintBoard()
	return status==2

# Play2 is random
def Play2():
	status=0
	while status==0:
		status = CBoard.Move(randint(0, 7), randint(0, 7), randint(0, 7), randint(0, 7), 0)
	CBoard.PrintBoard()
	return status==2

if __name__ == '__main__':
	CBoard = ChessBoard(Height=3, Transition=0.1)
	Player = Player(CBoard, WhitePlay=Play1, BlackPlay=Play2)
	CBoard.PrintBoard()

	for i in range(100):
		if Player.WhitePlay():
			break
		if Player.BlackPlay():
			break