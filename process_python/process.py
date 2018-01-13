import subprocess as p


f = open("1.txt","r")

a = p.Popen("javac "+input()+".java",shell=True)
b = p.Popen("java "+input(),stdout=p.PIPE,shell=True,stdin=f)
(output,err) = b.communicate()
p_status = b.wait()
print (output.decode("utf-8"))
