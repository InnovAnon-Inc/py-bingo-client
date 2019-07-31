from random import shuffle

def getLotto(width, height, extra): return Lotto(width * height + extra)

class Lotto(object):
	def __init__(self, n):
		data = list(range(1, n + 1))
		shuffle(data)
		self.data = data
	def draw(self):
		data = self.data
		next = data[-1]
		data = data[:-1]
		self.data = data
		return next
