from operator import __or__

from wc.composite_wc import CompositeWC
from wc.rows_cols_wc import RowsColsWC
from wc.diags_wc     import DiagsWC

class RowsColsDiagsWC(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __or__, [RowsColsWC(board, isSelected), DiagsWC(board, isSelected)])
