for case1 in range(int(input())):
    a = input()
    if len(a) == 10:
        if (a[0] != "0"):
            flag = True
            for k in a:
                try:
                    p = int(k)
                except:
                    flag = False
                    break
            if(flag):
                 print ("YES")
            else:
                 print ("NO")
        else:
            print ("NO")
    else:
        print ("NO")
