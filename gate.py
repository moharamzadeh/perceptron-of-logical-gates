class Gate():
	def __init__(self, type):
		self.states = [[1,1], [1,0], [0,1], [0,0]]
		self.type = type
		self.__insertTarget(type)

	def __insertTarget(self):
		type = self.type

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