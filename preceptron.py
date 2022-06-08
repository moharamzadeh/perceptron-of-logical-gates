class Preceptron():
	def __init__(self, alpha, astaneh):
		self.step = 0
		self.alpha = alpha
		self.y_in = None
		self.astaneh = astaneh
		self.X = None
		self.W = None
		self.bias = None

	def setInput(self, vector):
		pass

	def setWeight(self, vector):
		pass

	def y_function(self):
		if self.y_in > 0:
			return 1
		return 0

	def y_in_function(self):
		y_in = self.bias + (self.W[0]*self.X[0] + self.W[1]*self.X[1])
		return y_in 