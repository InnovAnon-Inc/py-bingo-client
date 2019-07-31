from operator import __and__, __or__

from wc.composite_wc import CompositeWC
from wc.diag_wc      import DiagWC
from wc.diag_t_wc    import DiagTWC
from wc.diag_rev_wc  import DiagRevWC
from wc.diag_trev_wc import DiagTRevWC

class XWC1(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __and__, [DiagWC(board, isSelected), DiagTWC(board, isSelected)])
class XWC2(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __and__, [DiagRevWC(board, isSelected), DiagTRevWC(board, isSelected)])

class XWC(CompositeWC):
	def __init__(self, board, isSelected):
		CompositeWC.__init__(self, board, isSelected, __or__, [XWC1(board, isSelected), XWC2(board, isSelected)])
