from board import transpose

from wc.wc      import WC
from wc.rows_wc import RowsWC

class ColsWC(RowsWC):
	def __init__(self, board, isSelected):
		RowsWC.__init__(self, transpose(board), isSelected)
