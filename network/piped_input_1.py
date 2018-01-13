from java.io import PipedInputStream as pi
from java.util import Scanner as S
from piped_output_1 import pip_out

class pip_input(object):
	def __init__(self):
		self.pi = pi()
		self.pipe = S(self.pi)

	def write_con(self):
		while self.pipe.hasNext():
			print (self.pipe.next()+" pipe-input")
		self.pi.close()
		self.pipe.close()


x = pip_input()
y = pip_out(x.pi)
y.call()
x.write_con()