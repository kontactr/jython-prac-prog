from java.util import StringTokenizer as ST
from java.io import BufferedReader as BR ,InputStreamReader as IR 
from java.lang import System as S

string = BR(IR(S.in)).readLine()
st1 = ST(string," ")
print (st1.countTokens())
while (st1.hasMoreTokens()):
	print (st1.nextToken())



