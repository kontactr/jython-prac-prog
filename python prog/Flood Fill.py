for case1 in range(int(input())):
    n,m,x1,y1,x2,y2 = list(map(int,input().strip(" ").split(" ")))
    x1-= 1
    y1-= 1
    x2-= 1
    y2-= 1
    li = [ list() for k in range(n) ]
    for j in range(n):
        val = list(map(int,input().strip(" ").split(" ")))
        li[j].extend(val)
    flag = True
    while (flag):
	
        if (x1==x2 and y1==y2):
            print ("YES")
            flag = False
        
        
        if ((x1-1) < 0):
            if ((y1-1) < 0):
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
                print (x1,y1,"Case-1-1")

                    
            elif ((y1+1) > m):
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
                print (x1,y1 , "Case-1-2")

            else:
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
         
                print (x1,y1,"Case-1-3")
                
            

        elif ((x1+1) > n):
            if ((y1-1) < 0):
                temp = 0 ; temp_x=-1 ;temp_y=-1
                if (li[x1][y1-1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1-1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y

                print (x1,y1,"Case-2-1")

            elif ((y1+1) > m):
                temp = 0
                temp_x=-1
                temp_y=-1
                if (li[x1][y1-1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1-1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
                print (x1,y1," Case-2-2")

            else:
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1][y1-1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1-1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
                print (x1,y1 , "Case-2-3")

        else:
            if ((y1-1) < 0):
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y

                print (x1,y1,"Case-3-1")

            elif ((y1+1) > m):
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1-1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1-1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y

                print (x1,y1,"Case-3-2")
				
            else:
                temp = 0 ; temp_x=-1 ; temp_y=-1
                if (li[x1+1][y1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1-1][y1] > li[x1][y1] ):
                    max_x , max_y = x1-1 , y1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1+1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1+1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if (li[x1][y1-1] > li[x1][y1] ):
                    max_x , max_y = x1+1 , y1-1
                    if (temp < li[max_x][max_y]):
                        temp = li[max_x][max_y]
                        temp_x = max_x
                        temp_y = max_y
                if(temp==0):
                    flag = False
                else:
                    x1 = temp_x
                    y1 = temp_y
            print (x1,y1 , "Case-3-3")
        
            
    if(flag == False):
        print ("NO")
