from wc.wc import WC

class DiagWC(WC):
	def __init__(self, board, isSelected):
		WC.__init__(self, board, isSelected)
		self.width  = board.width
		self.height = board.height
	def isWin(self):
		K = min(self.width, self.height)
		for Y in range(self.height - K + 1):
			if sum((self.isSelected(self.board.board[Y + y][y]) for y in range(K))) is K: return True
		return False
