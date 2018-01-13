from java.io import Serializable as S
from java.io import ObjectOutputStream as oos

class Employee(S):
	name , age , add = None , None , None
	
	def __init__(self,name,age,add):
		self.name = name
		self.age = age
		self.add  = add

	def emp_obj(self,obj):
		return Employee(obj.name,obj.age,obj.add)

	def display(self):
	        print ("name: "+str(self.name)+"\nage: "+str(self.age)+"\nadd: "+str(self.add))


emp_1 = Employee("y1",10,"India")
emp_2 = Employee("y2",10,"India")
file_write = open("file7.txt","w")

os = oos(file_write)
os.writeObject(emp_1)
os.writeObject(emp_2)

file_write.close()

