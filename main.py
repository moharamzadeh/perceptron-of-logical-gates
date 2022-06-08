from preceptron_gate import *

def main(gate, alpha, w1, w2):
	W_array = [w1, w2]
	prec = Preceptron_Gate(gate=gate, alpha=alpha, weitghts=W_array)
	for i in range(100):
		prec.nextIteration()
	
	return prec.W, prec.bias