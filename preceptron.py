class Preceptron():
	def __init__(self, alpha, datas, targets, weitghts):
		self.step = 0
		self.inputIndex = self.step % 4
		self.alpha = alpha
		self.__alldatas = datas
		self.targets = targets
		self.W = weitghts
		self.bias = 0

	def nextIteration(self):
		error = self.__error_in_step()
		if error != 0:
			self.__changeW_in_step()
			self.__changeBias_in_step()
			self.step =+ 1
			return True
		self.step += 1
		return False

	def __changeW_in_step(self):
		newW = self.newW_in_step()
		self.W = [self.W[0]+newW[0], self.W[1]+newW[1]]

	def __changeBias_in_step(self):
		changeBias = self.__errorStep()
		return changeBias

	def get_datas_in_step(self):
		return self.__alldatas[self.inputIndex]

	def newW_in_step(self):
		newW1 = self.__error_in_step()*self.get_datas_in_step()[0]
		newW2 = self.__error_in_step()*self.get_datas_in_step()[1]
		newW = [newW1, newW2]
		return newW

	def __y_function_in_step(self):
		if self.__y_in_function_in_step() > 0:
			return 1
		return 0

	def __y_in_function_in_step(self):
		X_data = self.get_datas_in_step()
		y_in = self.bias + (self.W[0]*X_data[0] + self.W[1]*X_data[1])
		return y_in

	def __error_in_step(self):
		err = self.targets[self.inputIndex] - self.__y_function_in_step()
		return err