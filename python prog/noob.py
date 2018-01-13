st = ""
v = int(input())
l = v
if (v == 1):
    print ("z")
else:
    v = (v+1) // 2
    while (v != 0):
        st += chr(123-v)
        v -= 1
    if(l%2 == 0):
        print (st[::-1]+st[::])
    else:
        print (st[:0:-1]+st[::])
    
