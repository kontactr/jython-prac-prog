a = int(input())
di = {}
arr = list(map(int,input().strip(" ").split(" ")))
for x in arr:
    if x in di:
        di[x] = di[x] + 1
    else:
        di[x] = 1
for y in range(int(input())):
    qu = int(input())
    print (di[qu])
