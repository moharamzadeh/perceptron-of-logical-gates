class Preceptron():
	def __init__(self, alpha):
		self.step = 0
		self.alpha = alpha

	def setInput(self, vector):
		self.X = vector

	def setWeight(self, vector):
		self.W = vector

	def setBias(self, value):
		self.bias = value

	def y_function(self):
		if self.y_in > 0:
			return 1
		return 0

	def y_in_function(self):
		y_in = self.bias + (self.W[0]*self.X[0] + self.W[1]*self.X[1])
		return y_in 