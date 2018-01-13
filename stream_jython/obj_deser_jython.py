from java.io import ObjectInputStream as ois
#from java.io import FileInputStream as fi
#from java.io import Serializable 
from obj_ser_jython import *
#from java.lang import Object
from org.python.util import PythonObjectInputStream as po

file_read = open("file7.txt","r")

temp = Employee(None,None,None)

		
os =  po(file_read) 
while True:
	try:
		k = os.readObject()
		k.display()
	except:
		break
file_read.close()

#FI = fi("file7.txt")

#os = ois(FI)
#print (os.readObject())

#FI.close()
