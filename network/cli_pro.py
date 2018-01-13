from java.net import Socket
from java.io import PrintStream
from java.io import InputStream
from java.io import OutputStream
from java.util import Scanner
from java.lang import Process
from java.lang import Runtime

class client(object):
	def __init__(self):
		self.s = Socket("127.0.0.1",777)

	def start_com(self):
		s_is = Scanner(self.s.getInputStream())
		file_name = s_is.nextLine()
		print (file_name)
		pro = Runtime.getRuntime().exec(file_name)
		try:
			pro_os = PrintStream(pro.getOutputStream())
		except:
			pass
		print ("reached")
		try:
			f = open(raw_input("Enter input file name: "),"r") 
			lp = []
			print (str(f)+" file")
			for k in f:
				lp.append(str(k))
			for k in lp:
				pro_os.print(k)
		except:
			pass
		finally:
			pro_os.close()
		pro_is = Scanner(pro.getInputStream())
		s_os = PrintStream(self.s.getOutputStream())
		s_os.println(file_name+" recieved")
		while pro_is.hasNext():
			s_os.println(pro_is.nextLine())
		s_is.close()
		s_os.close()
		self.s.close()

client().start_com()