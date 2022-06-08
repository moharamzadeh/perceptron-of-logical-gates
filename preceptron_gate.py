from preceptron import Preceptron
from gate import *

class Preceptron_Gate(Preceptron):
	def __init__(self, alpha, datas, targets, weitghts, gate):
		super().__init__(alpha, datas, targets, weitghts)
		self.gate = Gate(type=gate)
		self.setDatas = self.gate.states
		self.setTargets = self.gate.target

	def getStateX(self):
		self.gate.getState(self.step)