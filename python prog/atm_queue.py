a , g = int(input()) , 1
st = input().strip(" ").split(" ")
st = list(map(int,st))
for k in range(len(st)-1):
    if st[k] < st[k+1] or st[k] == st[k+1]:
        pass
    else:
        g += 1
print (g)
