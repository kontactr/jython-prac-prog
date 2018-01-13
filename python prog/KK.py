import math
size = input()
li = list(map(int,input().strip(" ").split(" ")))
for q in range(int(input())):
    st , en= list(map(int,input().strip(" ").split(" ")))
    mul = 1
    count = 1
    for k in range(st-1,en):
        mul *= li[k]
    while (mul%2 == 0):
        count *= 2
        mul = mul // 2
    print (int(math.log2(count)))
