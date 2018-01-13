from java.lang import ProcessBuilder as pb
from java.lang import Process as P
from java.io import File as F
from java.io import InputStream as IS
from java.io import OutputStream as OS
from java.io import InputStreamReader as ISR
from java.io import OutputStreamWriter as OSR
from java.io import BufferedReader as BR
from java.io import BufferedWriter as BW
from java.util import Scanner as S
from java.net import URL as U
from java.net import URLConnection as UC


with open("url.txt","r") as f: 
	global url
	url = U(f.readline())

conn = url.openConnection()
in_st_url = BR(ISR(conn.getInputStream()))

with open("Temp_2.py","w") as f:
	 while True:
	 	try:
			f.write(in_st_url.readLine()+"\n")
		except:
			break

builder = pb(["python","Temp_2.py"])
builder.directory(F("C:\\Users\\Sony\\Desktop\\jython-prac-prog\\network"))
process  = builder.start()
p_i = BR(ISR(process.getInputStream()))
p_o = BW(OSR(process.getOutputStream()))


with  open("input.txt","r") as f:
	global li
	li = f.readlines()

for k in li:
	p_o.write(k)

p_o.flush()
p_o.close()

s = S(p_i)

while s.hasNextLine():
	print (s.nextLine())

