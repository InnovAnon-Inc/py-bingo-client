from operator import __and__

from wc.composite_wc import CompositeWC
from wc.rows_wc      import RowsWC
from wc.cols_wc      import ColsWC

class TWC(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __and__, [RowsWC(board, isSelected), ColsWC(board, isSelected)])
