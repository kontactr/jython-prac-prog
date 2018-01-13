def div(num):
    count = 1
    for x in range(1,num//2+1):
        if (num % x == 0):
            count += 1
    print (count)
    return count

case1 = int(input())
for y in range(case1):
    st = input()
    sum1 = 0
    for k in st:
        sum1 += ord(k.lower()) - 96
    print (sum1)
    if (div(sum1) >= len(st)):
        print ("IN")
    else:
        print ("OUT")
