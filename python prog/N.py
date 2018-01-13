a = int(input())
print ("*"+(" "*(a-2))+"*")
i = 0
for k in range(2,a):
    print ("*"+(" "*i)+"*"+(" "*(a-3-i))+"*")
    i += 1
print ("*"+(" "*(a-2))+"*")
