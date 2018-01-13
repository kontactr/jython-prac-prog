n , m = input().split(" ")
di = {}
l = set()
for k in range(int(m)):
    a , b = input().split(" ")
    l.add(a)
    l.add(b)
print (len(l)," ".join(l),sep="\n",end="")
