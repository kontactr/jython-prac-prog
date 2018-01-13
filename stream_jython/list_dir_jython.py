from java.io import File
import os

co = raw_input("enter directory: ")
print (co)


f_d = File(co)
print ("process:")
if(f_d.exists()):
   if(f_d.isDirectory()):
	os.chdir(co) #must use otherwise you got all containts as directory
	for k in f_d.list():
		if os.path.isfile(k):
			print (k+"  - file")
		else:
			print (k+"  - directory")
		
   else:
	print ("not directory")
else:
	print ("not exist")


print ("end:")


