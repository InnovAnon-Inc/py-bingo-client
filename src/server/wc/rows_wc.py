from wc.wc import WC

class RowsWC(WC):
	def __init__(self, board, isSelected):
		WC.__init__(self, board, isSelected)
	def isWin(self):
		for row in self.board.board:
			if sum((self.isSelected(x) for x in row)) is len(row): return True
		return False
