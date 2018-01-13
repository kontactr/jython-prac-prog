from java.io import PipedInputStream as PIS
from java.io import PipedOutputStream as POS
from java.util import Scanner as SC
from java.lang import System
from java.lang import Thread
from java.io import FileReader 
from java.io import OutputStream

class input_file(Thread):
	def __init__(self):
		self.pis = PIS()
		#self.wt = write_thread

	def run(self):
		#self.wt.join()
		while self.pis.available():
			System.out.print(chr(self.pis.read()))


class output_file(Thread):
	def __init__(self,pi):
		self.pout = POS(pi)
		self.file_name = FileReader(SC(System.in).nextLine())

	def run(self):
		file_sc = SC(self.file_name)
		while file_sc.hasNext():
			self.pout.write(file_sc.nextLine()+"\n")

x = input_file()
y = output_file(x.pis)
y.start()
y.join()
x.start()
x.join()