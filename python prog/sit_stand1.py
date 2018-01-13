

size,hour = input().split(" ")
s = input().split(" ")
p = s[::]
l = [0]
flag = True
while (flag):
    if "1" in p:
        val = p.index("1")
        print (val)
        l.append(l[-1]+val+1)
        p = p[val+1::]
        
    else:
        flag = False
l.pop(0)
for r in range(int(hour)):
    print (l)
    for x in range(len(l)):
        if (x>0 and x<len(l)-1):
            if l[x] - l[x-1] == 2:
                l.append((l[x]+l[x-1])//2)
            if l[x+1] - l[x] == 2:
                l.append((l[x]+l[x-1])//2)
        elif (x == 0):
            if l[x+1] - l[x] == 2:
                l.append((l[x]+l[x-1])//2)
        else:
            if l[x] - l[x] == 2:
                l.append((l[x]+l[x-1])//2)

    l = list(set(l))
    l.sort()
print (l)
                
                
