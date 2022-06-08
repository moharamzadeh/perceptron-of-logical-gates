class Gate():
	def __init__(self, type):
		self.type = type

	def __insertTable(self):
		type = self.type
		self.states = [[1,1], [1,0], [0,1], [0,0]]

		if type == 'AND':
			self.target = [1, 0, 0, 0]
		elif type == 'OR':
			self.target = [1, 1, 1, 0]
		elif type == 'NOR':
			self.target = [0, 0, 0, 1]
		elif type == 'NAND':
			self.target = [0, 1, 1, 0]
		else:
			raise 'state not exist'