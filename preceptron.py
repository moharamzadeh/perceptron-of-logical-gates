class Preceptron():
	def __init__(self, alpha, astaneh):
		self.step = 0
		self.alpha = alpha
		self.y_in = None
		self.astaneh = astaneh

	def y_function(self):
		if self.y_in > 0:
			return 1
		return 0

	def y_in_function(self, bayas, X, W):
		iteration = len(X)
		for i in iteration:
			pass