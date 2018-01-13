def div(num):
    count = 0
    for x in range(1,int(num//2)+1):
        if num % x == 0:
            count += 1
    return count+1

for test in range(int(input())):
    print (div(int(input())) - 1)
