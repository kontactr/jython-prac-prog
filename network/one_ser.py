from java.net import ServerSocket as SS
from java.net import Socket as SO
from java.io import InputStream
from java.io import OutputStream
from java.io import PrintStream as PS
from java.util import Scanner as S


SS_1 = SS(777)
SO_1 = SS_1.accept()
IS_1 = S(SO_1.getInputStream())
OS_1 = PS(SO_1.getOutputStream())
while True:
	if IS_1.hasNext():
		print (IS_1.next())
		print (OS_1.println("received..."))
	else:
		break