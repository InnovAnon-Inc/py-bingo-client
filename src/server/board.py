from random import randint

from lotto import getLotto
from wc.wc import WC

def getBoard(width=5, height=5, extra=75 - 5 * 5):
	lotto = getLotto(width, height, extra)
	board = [[lotto.draw() for _ in range(width)] for __ in range(height)]
	# TODO free spaces
	return Board(board, width, height)

def transpose(board): return Board(WC.transpose(board.board), board.height, board.width)

def reverse(board):   return Board(WC.reverse(board.board),   board.width,  board.height)

class Board(object):
	FREE_SPACE = -1

	def __init__(self, board, width, height):
		self.board  = board
		self.width  = width
		self.height = height

	#def __str__(self):
		#return str(self.board)
		#return "\n".join((" ".join(("%3s" % (x if x is not Board.FREE_SPACE else 'X') for x in row)) for row in self.board))
	def toString(self, isSelected):
		s = "\n".join((" ".join(("%3s" % (x if not isSelected(x) else 'X') for x in row)) for row in self.board))
		print(s)
		return s
		

	#def __iter__(self): return iter(self.board)
