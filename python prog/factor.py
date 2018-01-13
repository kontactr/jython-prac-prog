def factor(num):
    count = 1
    for x in range(2,num//2+1):
        if num % x == 0:
            count += 1
    if (num == 1):
        return count
    else:
        return count+1

for x in range(int(input())):
    x1 = map(int,input().strip(" ").split(" "))
    for y in x1:
        print (factor(y))
    
