from java.io import FileWriter
from java.io import File
from java.io import FileReader

f1 = File("file2.txt")
fr = FileReader(f1)
f2 = File("file3.txt")
fw = FileWriter(f2)

while True:
	ch = fr.read()
	if ch != -1:
		fw.write(ch)
	else:
		break

fr.close()
fw.close()

