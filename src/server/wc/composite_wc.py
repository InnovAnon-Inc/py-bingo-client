from functools import reduce

from wc.wc      import WC

class CompositeWC(WC):
	def __init__(self, board, isSelected, op, wcs):
		WC.__init__(self, board, isSelected)
		self.wcs = wcs
		self.op  = op
	def isWin(self): return reduce(self.op, map(lambda wc: wc.isWin(), self.wcs))
