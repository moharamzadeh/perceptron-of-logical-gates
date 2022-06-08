class Preceptron():
	def __init__(self, alpha):
		self.step = 0
		self.alpha = alpha
		self.W = [0, 0]
		self.bias = 0

	def setInput(self, vector):
		self.X = vector

	def setWeight(self, vector):
		self.W = vector

	def setBias(self, value):
		self.bias = value

	def y_function(self):
		if self.__y_in_function() > 0:
			return 1
		return 0

	def __y_in_function(self):
		y_in = self.bias + (self.W[0]*self.X[0] + self.W[1]*self.X[1])
		return y_in

	def __error(self, value, targetValue):
		pass