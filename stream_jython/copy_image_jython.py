from java.io import FileInputStream as FI
from java.io import FileOutputStream as FO
from java.io import BufferedInputStream as BI
from java.io import BufferedOutputStream as BO

file_read = FI("image1.png")
buffer_read = BI(file_read)

file_write = FO("imag2.png")
buffer_write = BO(file_write)

while True:
	ch = buffer_read.read()
	if ch != -1:
		buffer_write.write(ch)
	else:
		break

buffer_read.close()
file_read.close()
buffer_write.close()
file_write.close()
