from java.net import Socket as s
from java.io import InputStream as Is
from java.io import OutputStream as os
from java.io import FileReader as fr
from java.io import BufferedReader as br
from java.io import InputStreamReader as isr
from java.io import PrintStream as ps
from java.lang import System
from datetime import datetime as d

x_time = d.now()
s1 = s("localhost",766)
os1 = ps(s1.getOutputStream())
os2 = br(isr(System.in))
x = os2.readLine()
os1.println(x)
is1 = br(isr(s1.getInputStream()))
while True:
	try:
		p = is1.readLine()
		if(p==None):
			break
		print (p)
	except:
		print ("end")
		break
os1.close()
os2.close()
is1.close()
s1.close()
y_time = d.now()
print ("required time: %f "%((y_time-x_time).total_seconds()))