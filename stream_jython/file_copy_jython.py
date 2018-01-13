from java.io import FileInputStream as  FI
from java.io import FileOutputStream as FO

file_read = FI("file1.txt")
file_write = FO("file2.txt")
while True:
	ch = file_read.read()
	if ch != -1:
		file_write.write(chr(ch))
	else:
		break

file_read.close()
file_write.close()





