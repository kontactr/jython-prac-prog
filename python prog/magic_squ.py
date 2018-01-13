a = int(input())
l = list(range(1,a+1))
for x in range(a):
    print (" ".join(map(str,l[x:]+l[:x])))
