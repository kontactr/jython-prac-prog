for case1 in range(int(input())):
    size = int(input())
    l = []
    for x in range(size):
        l.append(input())
    flag = True
    for x in range((size+1)//2):
        if l[x] != l[-1-x]:
            flag = False
            break
    if(flag):
        for x in range((size+1)//2):
            for y in range(size):
                if (l[y][x] != l[y][-1-x]):
                    flag = False
                    break
        if(flag):
                    print ("YES")
        else:
                    print ("NO")
    else:
        print ("NO")
    
