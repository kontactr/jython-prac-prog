from java.nio.file import Paths
from java.nio.file import Path
from java.io import File

p=Paths.get("home","pi","Desktop","jython-prac-prog","stram_jython","file2.txt")

x = p.toFile()

x = File(x.getName())
print (x.isFile())

f = File("image1.png") 
print (f.getName())
print ("length",f.length())
print ("Execute",f.canExecute())
print ("read",f.canRead())
print ("write",f.canWrite())
print ("path",f.getPath())
print ("Directory",f.isDirectory())
print ("parent",f.getParent())

