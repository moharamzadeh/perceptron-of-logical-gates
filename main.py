from preceptron_gate import *

def main(gate, alpha, w1, w2):
	W_array = [w1, w2]
	prec = Preceptron_Gate(gate=gate, alpha=alpha, weitghts=W_array)
	for i in range(100):
		break_step = 0
		if break_step > 4:
			break
		error_nadashtan = prec.nextIteration()
		if error_nadashtan:
			break_step += 1
	
	return prec.W, prec.bias