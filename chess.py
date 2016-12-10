#!/usr/bin/python
	
# I need Board
# I need Pieces
# I need Players
# I need Rules

def DrawBoard(Texture="[][][]", Height=3):
	White	= "\033[97m{}\033[00m"
	Black	= "\033[98m{}\033[00m"
	for Boxes in range(4):
		for i in range(Height):
			print(
				White.format(Texture)+Black.format(Texture)+
				White.format(Texture)+Black.format(Texture)+
				White.format(Texture)+Black.format(Texture)+
				White.format(Texture)+Black.format(Texture)
			)
		for i in range(Height):
			print(
				Black.format(Texture)+White.format(Texture)+
				Black.format(Texture)+White.format(Texture)+
				Black.format(Texture)+White.format(Texture)+
				Black.format(Texture)+White.format(Texture)
			)

if __name__ == '__main__':
	DrawBoard(Texture="0000", Height=2)