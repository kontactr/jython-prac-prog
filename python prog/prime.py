a = int(input())
s = ""
if (a == 1):
    print (s)
else:
    for i in range(2,a+1):
        flag = True
        for j in range(2,int(i**0.5+1)):
            if i%j == 0:
                flag = False
                break
        if(flag):
                s += str(i) + " "
    print (s.strip(" "))
    
            
