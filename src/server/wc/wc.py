from abc import ABCMeta
from abc import abstractmethod

class WC(object, metaclass=ABCMeta):
	def __init__(self, board, isSelected):
		self.board      = board
		self.isSelected = isSelected
	@abstractmethod
	def isWin(self): raise Exception()
	@staticmethod
	def transpose(board): return list(zip(*board))
	@staticmethod
	def reverse(board):   return [row[::-1] for row in board]
