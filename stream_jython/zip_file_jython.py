from java.io import File as F
from java.io import FileInputStream as FI
from java.io import FileOutputStream as FO
from java.io import BufferedInputStream as BI
from java.io import BufferedOutputStream as BO
from java.util.zip import DeflaterOutputStream as DO

file_read = F("file4.txt")
file_write = F("file5.txt")

bi = BI(FI(file_read))
bo = BO(DO(FO(file_write)))

while True:
	val = bi.read()
	if val != -1:
		bo.write(val)
	else:
		break

bi.close()
bo.close()
