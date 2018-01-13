date = input().strip(" ").split(",")
dd , mm , yy = 0 , 0 , 0
for k in range(len(date)):
            for y in range(len(date)):
                temp = int(date[k]+date[y])
                if k != y and yy < temp:
                    if temp >= 0 and temp <=99:
                        yy = temp
                    else:
                        break
yy = str(yy)
if len(yy) == 1:
    date.remove(0)
    date.remove(yy)
else:
    date.remove(yy[0])
    date.remove(yy[1])
yy = int(yy)
if (yy>=0 and yy<=99):    
        for k in range(len(date)):
            for y in range(len(date)):
                temp = int(date[k]+date[y])
                if k != y and mm < temp:
                    if temp >= 1 and temp <=12:
                        mm = temp
                    else:
                        break
        mm = str(mm)
        if len(mm) == 1:
            date.remove(0)
            date.remove(mm[0])
        else:
            date.remove(mm[0])
            date.remove(mm[1])
        mm = int(mm)       
        if ( mm >= 1 and mm <=12):
            flag = 0
            if mm in [1,3,5,7,8,10,12]:
                flag = 0
            elif mm in [4,6,9,11]:
                flag = 1
            elif mm in [2]:
                flag = 2
            else:
                pass
            for k in range(len(date)):
                for y in range(len(date)):
                    temp = int(date[k]+date[y])
                    if k!= y and dd < temp:
                        if (flag == 1) and temp >= 1 and temp <=30:
                            dd = temp
                        elif  (flag == 0) and temp >= 1 and temp <=31:
                            dd = temp
                        elif (flag == 2):
                            if int(yy)%4 == 0:
                                if temp >=1 and temp <=29:
                                    dd = temp
                            else:
                                if temp >=1 and temp <=28:
                                    dd = temp
                        else:
                            break
            if (dd >= 1 and dd <=31):
                mm , dd, yy= str(mm),str(dd),str(yy)
                if len(yy) == 1:
                   yy = "0"+yy
                if len(mm) == 1:
                  mm = "0"+mm
                if len(dd) == 1:
                  dd = "0"+dd
                print (yy,mm,dd,sep="/")            
            else:
                  print ("Impossible")
            
            
        else:
            print ("Impossible")
else:
    print ("Impossible")
