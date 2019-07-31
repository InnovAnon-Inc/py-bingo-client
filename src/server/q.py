class Q(object):
	def __init__(self, min_n, max_n, timeout, max_timeout, players):
		self.min_n = min_n
		self.max_n = max_n
		self.timeout     = timeout
		self.max_timeout = max_timeout
		self.players     = players

		self.last_tick     = 0
		self.total_timeout = 0
		self.timeout_flag = False
		self.n             = 0
	def isEnoughPlayers(self): return len(self.players) >= self.min_n
	def isMaxPlayers(self):    return len(self.players) >= self.max_n
	def isMaxTimeout(self):    return self.max_timeout and self.total_timeout >= self.max_timeout
	def isTimeOut(self):       return self.timeout_flag
	def isDone(self):          return self.isEnoughPlayers() and (self.isTimeOut() or self.isMaxTimeout()) or self.isMaxPlayers()

	def tick(self, T):
		if self.last_tick >= self.timeout: self.timeout_flag = True
		old_n = self.n
		self.n = len(self.players)
		if old_n < self.n:
			self.last_tick    = 0
			self.timeout_flag = False
		else: self.last_tick = self.last_tick + T
		self.total_timeout = self.total_timeout + T

