from java.net import InetAddress as ip

website = raw_input("Enter website name: ")


#request serviced:
print (ip.getByName(website))

print ()
print ("all address: ")
for k in ip.getAllByName(website):
	print (k)
