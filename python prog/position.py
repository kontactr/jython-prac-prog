a = int(input())
li = []
for k in range(1,a+1):
    i = input()
    li.append(i)
    li.sort()
    print (li.index(i))
