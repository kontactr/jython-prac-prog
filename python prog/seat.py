s_l = {1:(12,"WS"),2:(11,"MS"),3:(10,"AS"),4:(9,"AS"),5:(8,"MS"),6:(7,"WS")}
s_l1 = {12:(1,"WS"),0:(1,"WS"),11:(2,"MS"),10:(3,"AS"),9:(4,"AS"),8:(5,"MS"),7:(6,"WS")}
a = int(input())
for k in range(a):
    val = int(input())
    if val in s_l:
        temp = s_l[val]
        print (str(temp[0])+" "+temp[1])
    elif val >12:
        temp = int(val % 12)
        pos = ""
        val1 = 0
        if temp in s_l:
            
            val1 = s_l[temp][0]
            
            pos = s_l[temp][1]
            while (val > val1):
                val1 += 12
        else:
            val1 = s_l1[temp][0]
            pos = s_l1[temp][1]
            while (val > val1):
                val1 += 12
            val1 -= 12
        print (val1,pos)
    else:
        if val in s_l1:
            temp = s_l1[val]
            print (str(temp[0])+" "+temp[1])
            
