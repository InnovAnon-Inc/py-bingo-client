from operator import __or__

from wc.composite_wc import CompositeWC
from wc.rows_wc      import RowsWC
from wc.cols_wc      import ColsWC

class RowsColsWC(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __or__, [RowsWC(board, isSelected), ColsWC(board, isSelected)])
