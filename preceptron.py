class Preceptron():
	def __init__(self, alpha, datas, targets, weitghts):
		self.step = 0
		self.inputIndex = self.step % 4
		self.alpha = alpha
		self.__alldatas = datas
		self.targets = targets
		self.W = weitghts
		self.bias = 0

	def __changeW_in_step(self, X):
		changeW = [self.__errorStep*X[0], self.__errorStep*X[1]]
		return changeW

	def __changeBias_in_step(self,):
		changeBias = self.__errorStep()
		return changeBias

	def newW_in_step(self):
		pass

	def __y_function_in_step(self):
		if self.__y_in_function() > 0:
			return 1
		return 0

	def __y_in_function_in_step(self):
		y_in = self.bias + (self.W[0]*self.X[0] + self.W[1]*self.X[1])
		return y_in

	def __error_in_step(self):
		err = self.targets[self.inputIndex] - self.y_function()
		return err