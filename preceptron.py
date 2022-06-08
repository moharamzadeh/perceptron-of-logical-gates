class Preceptron():
	def __init__(self, alpha, datas, targets, weitghts):
		self.step = 0
		self.inputIndex = self.step % 4
		self.alpha = alpha
		self.datas = datas
		self.targets = targets
		self.W = weitghts
		self.bias = 0

	def changeW(self, X):
		changeW = [self.__errorStep*X[0], self.__errorStep*X[1]]
		return changeW

	def changeBias(self,):
		changeBias = self.__errorStep()

	def y_function(self):
		if self.__y_in_function() > 0:
			return 1
		return 0

	def __y_in_function(self):
		y_in = self.bias + (self.W[0]*self.X[0] + self.W[1]*self.X[1])
		return y_in

	def __error(self, targetValue):
		err = targetValue - self.y_function()
		return err