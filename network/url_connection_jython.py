from java.io import InputStreamReader as br
from java.io import InputStream as i 
from java.io import OutputStreamWriter as bw
from java.io import BufferedReader as br1
from java.io import BufferedWriter as bw1
from java.net import URL as u
from java.net import URLConnection as uc
#from datetime import datetime as d
from java.util import Date as d
from java.lang import Object as O
from java.lang import Character as C
from java.lang import ProcessBuilder
from java.lang import Runtime
from java.lang import System
from java.lang import Thread as t

#val = raw_input("Enter url: ")
with open("url.txt","r") as f: 
	global url1 
	url1 = u(f.readline())

conn = url1.openConnection()
print (d(conn.getDate()).toString())

input_stream = conn.getInputStream()
print (input_stream)
f = open("prog.py","w")
try:
	x = None
	while x!=-1:
		x = input_stream.read()
		try:
			x = chr(x)
			f.write(x)
		except:
			break
finally:
	f.close()
print (f.closed)
#q = System.getenv()
#for k in q.items():
#	print (k)
#System.getenv("user.dir")
import os
from java.io import File
builder = ProcessBuilder(["python", "prog.py"])
builder.directory(File(os.getcwd()))
process = builder.start();
x = br1(br(process.getInputStream()))
y = bw1(bw(process.getOutputStream()))
y.write(10)
y.flush()
y.close()
from java.util import Scanner as S
X = S(x)
print (X.nextLine())
print (X.nextLine())
t.sleep(5000)
print (X.nextLine())
#while x!=-1:
#	b = x.read()
#	print (chr(b))

print ("end")


