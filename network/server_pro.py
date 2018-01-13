from java.net import ServerSocket
from java.net import Socket
from java.io import InputStream
from java.io import OutputStream
from java.io import PrintStream
from java.util import Scanner
from java.lang import Thread

class server(Thread):
	def __init__(self,file_name):
		self.list = []
		self.ss = ServerSocket(777)
		f =  open(file_name,"r")
		self.list = f.readlines()

	def run(self):

		while len(self.list):
			s = self.ss.accept()
			server_multi(s,self.list[0]).start()
			self.list.pop(0)


class server_multi(Thread):
		def __init__(self,so,li):
			self.so = so
			self.li = li

		def run(self):
			st_os = PrintStream(self.so.getOutputStream())
			st_os.println(self.li)
			print ("writting complete")
			st_is = Scanner(self.so.getInputStream())
			while st_is.hasNext():
				print (st_is.nextLine())
			st_os.close()
			st_is.close()
			self.so.close()

server("task.txt").start()
