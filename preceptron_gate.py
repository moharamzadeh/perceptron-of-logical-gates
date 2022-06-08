from preceptron import Preceptron
from gate import *

class Preceptron_Gate(Preceptron):
	def __init__(self, gate, alpha, weitghts):
		self.gate = Gate(type=gate)
		datas = self.gate.states
		targets = self.gate.target
		super().__init__(alpha, datas, targets, weitghts)

	def getStateX(self):
		self.gate.getState(self.step)