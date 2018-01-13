from java.net import Socket as SO
from java.io import InputStream
from java.io import OutputStream
from java.io import PrintStream as PS
from java.util import Scanner as S
from java.io import File 

SO_1 = SO("127.0.0.1",777)
IS_1 = S(SO_1.getInputStream())
OS_1 = PS(SO_1.getOutputStream())
S1 = S(File("input.txt"))
while True:
	if S1.hasNext():
		OS_1.println(S1.next())
		print(IS_1.next())
	else:
		break
