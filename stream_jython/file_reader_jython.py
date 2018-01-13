from java.io import BufferedReader as BR
from java.io import FileReader as FR
from java.io import BufferedWriter as BW
from java.io import FileWriter as FW
from java.io import File as F

file_r = F("file3.txt")
file_w = F("file4.txt")

br = BR(FR(file_r))
bw = BW(FW(file_w))

while True:
	line = br.readLine()
	if line != None:
		bw.write(line+"\n")
	else:
		break


br.close()
bw.close()
