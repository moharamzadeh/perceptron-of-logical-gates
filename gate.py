class Gate():
	def __init__(self, type):
		self.type = type

	def __insertTable(self):
		type = self.type
		self.states = [[1,1], [1,0], [0,1], [0,0]]
		target = None

		if type == 'AND':
			target = [1, 0, 0, 0]
		elif type == 'OR':
			target = [1, 1, 1, 0]
		elif type == 'NOR':
			target = [0, 0, 0, 1]
		elif type == 'NAND':
			target = [0, 1, 1, 0]