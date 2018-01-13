import java.util.HashSet as hs
a = hs()
if type(a) == hs:
	with open("name.txt","r") as file:
		for line in file:
			 str_dat = line.strip("\n")
			 a.add(str_dat)
for data in a:
	print (data)
#print ("data")