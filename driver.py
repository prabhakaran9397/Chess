from chess import ChessBoard

if __name__ == '__main__':
	CBoard = ChessBoard(3, 1)
	CBoard.PrintBoard()
	CBoard.Move(1, 3, 3, 3)	# Move the pawn
	CBoard.PrintBoard()