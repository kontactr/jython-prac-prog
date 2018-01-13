for case1 in range(int(input().strip(" "))):
    ini ,fin = input().strip(" ").split(" ")
    ind_i , ind_f = -1 , -1
    flag = True
    while (True):
        try:
            ind_i , ind_f = [ini[ind_i+1::].index("A") , fin[ind_f+1::].index("A")]
            #print (ind_i)
            #print (ind_f)
            if ind_f < ind_i:
                if ini[ind_f:ind_i+1] == ("#"*(ind_i-ind_f))+ini[ind_i]:
                    #print (fin[ind_f]+("#"*(ind_i-ind_f-1))+ini[ind_i])
                    ini = fin[ind_f]+("#"*(ind_i-ind_f-1))+fin[ind_i] + ini[ind_i+1:]
            elif ind_f == ind_i:
                #print ("hello - 1")
                continue
            else:
                #print ("hello - 2")
                flag = False
                break
        except:
             break
    #print (ini,fin)
    if(flag):
        ind_i , ind_f = -1 , -1
        while (True):
            try:
                ind_i , ind_f = [ini[ind_i+1::].index("B") , fin[ind_f+1::].index("B")]
                if ind_f > ind_i:
                    if ini[ind_i:ind_f+1] == ("#"*(ind_f-ind_i))+ini[ind_f]:
                        ini = fin[ind_i]+("#"*(ind_f-ind_i-1))+fin[ind_f] + ini[ind_f+1:]
                elif ind_f == ind_i:
                    break
                else:
                    flag = False
                    break
            except:
                 break
        if(flag):
            print ("YES")
        else:
            print ("NO")
    else:
        print ("NO")

                
                     
