from wc.wc      import WC
from wc.diag_wc import DiagWC
from board      import transpose

class DiagTWC(DiagWC):
	def __init__(self, board, isSelected):
		DiagWC.__init__(self, transpose(board), isSelected)
