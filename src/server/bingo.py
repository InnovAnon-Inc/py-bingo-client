from random import choice

from board import getBoard
from board import Board
from lotto import getLotto

from wc.rows_cols_wc       import RowsColsWC
from wc.diags_wc           import DiagsWC
from wc.rows_cols_diags_wc import RowsColsDiagsWC
from wc.x_wc               import XWC
from wc.t_wc               import TWC
#from wc.box_wc             import BoxWC

class Bingo(object):
	def __init__(self, players):
		#print("Starting new Game(players=%s)" % (players,))
		#self.players = players

		#self.boards = []
		#for p in players:
		#	board = Board()
			#p.Send({"action" : "board", "board" : board.board})
		#	self.boards.append(board)
		width  = 6
		height = 5
		extra  = 75 - 5 * 5
		self.boards = {p : getBoard(width, height, extra) for p in players}

		self.lotto  = getLotto(width, height, extra)

		#self.WC = choice((RowsColsWC, DiagsWC, RowsColsDiagsWC, XWC, TWC, BoxWC))
		self.WC = choice((RowsColsWC, DiagsWC, RowsColsDiagsWC, XWC, TWC))

		self.history = []
	def __iter__(self): return iter(self.boards)
	def items(self): return self.boards.items()
	def tick(self):
		next = self.lotto.draw()
		self.history.append(next)
		#for p in self.players: p.Send({"action" : "draw", "draw" : next})
		self.last_draw = next
	#def isSelected(self): return lambda x: x is Board.FREE_SPACE or x in self.history
	def isSelected(self):
		def foo(x):
			#print("x: %s, history: %s" % (x, self.history))
			if x is Board.FREE_SPACE: return True
			if x in self.history:     return True
			#print("return False")
			return False
		return foo
	def isOver(self):
		#print(len(self.boards))
		if not len(self.boards): return True
		for board in self.boards.values():
			if self.WC(board, self.isSelected()).isWin(): return True
		return False
	def getResults(self):
		winners, losers = [], []
		for player, board in self.boards.items():
			if self.WC(board, self.isSelected()).isWin(): winners.append(player)
			else:                                       losers.append(player)
		return { "winners" : winners, "losers" : losers }
		#return winners, losers
	def DelPlayer(self, player):
		del self.boards[player]
