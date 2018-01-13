for case1 in range(int(input())):

    l = [input() for x in range(4)]
    p = [l[0][0]+l[1][1]+l[2][2] ,
         l[0][1]+l[1][2]+l[2][3] ,
         l[1][0]+l[2][1]+l[3][2] ,
         l[1][1]+l[2][2]+l[3][3] , l[0][2]+l[1][1]+l[2][0] ,
           l[0][3]+l[1][2]+l[2][1] ,
           l[1][2]+l[2][1]+l[3][0] ,
           l[1][3]+l[2][2]+l[3][1] ]

    flag = True
    for x in l:
        if ("x.x" in x) or (".xx" in x) or ("xx." in x):
            flag = False
            break
    if(not flag):
        print ("YES")
    else:
        for x in range(4):
            st = ""
            for y in range(4):
                st += l[y][x]
            if ("x.x" in st) or (".xx" in st) or ("xx." in st):
                flag = False
                break
        if(not flag):
            print ("YES")
        else:
            for x1 in p:
                if ("x.x" in x1) or (".xx" in x1) or ("xx." in x1):
                    flag = False
                    break
            if(not flag):
                print ("YES")
            else:
                print ("NO")
