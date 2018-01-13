size = int(input())
a1 = list(map(int,input().split(" ")))
a1.sort()
a2 = list(map(int,input().split(" ")))
a2.sort(reverse=True)
sum1 = 0
for x in range(size):
    sum1 += a1[x] * a2[x]
print (sum1)
