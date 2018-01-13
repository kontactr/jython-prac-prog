from java.net import ServerSocket
from java.net import Socket
from java.io import InputStream
from java.io import OutputStream
from java.io import PrintStream
from java.util import Scanner
from java.lang import Thread

class reg(Thread):
	i = 2
	def __init__(self,server):
		self.reg_obj_ip = server

	def run(self):
		print ("broad time...")
		if len(self.reg_obj_ip) > reg.i:
			reg.i+=5
			for k in self.reg_obj_ip:
				if k.isConnected() and  not(k.isClosed()):
					K = PrintStream(k.getOutputStream())
					K.println("BroadCast Message....")
				else:
					self.reg_obj_ip.remove(k)
		else:
			print ("here")
			Thread.sleep(5000)
		


class server(object):
	reg_obj_ip = []
	def __init__(self):
		self.ss = ServerSocket(8888)

	def start(self):
		while True:
			self.s = self.ss.accept()
			self.reg_obj_ip.append(self.s)
#			reg(self.reg_obj_ip).start()
			

# class stream_hand(Thread):
# 	def __init__(Self,s):
# 		Self.ss = s

# 	def run(Self):
# 		while True:
# 			if int(raw_input("Want read(1) or write(0): ")):
# 				k = Scanner(Self.ss.getInputStream())
# 				while k.hasNext():
# 					print (k.nextLine())
# 			else:
# 				PrintStream(Self.ss.getOutputStream()).print(raw_input("Enter input: "))




server().start()
