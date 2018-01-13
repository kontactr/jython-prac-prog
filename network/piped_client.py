import piped_interface as pii
from java.lang import Thread

class client():
	def __init__(self):
		self.obj = pii.obj
		print (pii.obj)

	def send_server(self):
		self.obj.po.println("hello world")
		Thread.wait()


client().send_server()