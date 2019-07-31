from wc.wc      import WC
from wc.diag_wc import DiagWC
from board      import reverse

class DiagRevWC(DiagWC):
	def __init__(self, board, isSelected):
		DiagWC.__init__(self, reverse(board), isSelected)
