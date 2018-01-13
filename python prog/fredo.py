size = int(input())
arr = input().split(" ")
di = {}
for x in arr:
    if x in di:
        di[x] = di[x]+1
    else:
        di[x] = 1

for x in range(int(input())):
    ty,fr = list(map(int,input().split(" ")))
    flag = True
    if(ty):
        for y in di:
            if (di[y] == fr):
                print (y)
                flag = False
                break
        if(flag):
            print (0)
    else:
        for y in di:
            if (di[y] >= fr):
                print (y)
                flag = False
                break
        if(flag):
            print (0)
    
