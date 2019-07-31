from operator import __or__

from wc.composite_wc import CompositeWC
from wc.diag_wc      import DiagWC
from wc.diag_t_wc    import DiagTWC
from wc.diag_rev_wc  import DiagRevWC
from wc.diag_trev_wc import DiagTRevWC

class DiagsWC(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __or__, [DiagWC(board, isSelected), DiagTWC(board, isSelected), DiagRevWC(board, isSelected), DiagTRevWC(board, isSelected)])
