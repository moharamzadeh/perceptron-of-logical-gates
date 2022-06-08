from preceptron import Preceptron
from gate import *

class Preceptron_Gate(Preceptron):
	def __init__(self, alpha, gate):
		super().__init__(alpha)
		self.gate = Gate(type=gate)

	def getStateX(self):
		self.gate.getState(self.step)