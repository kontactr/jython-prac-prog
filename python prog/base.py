def gcd(a,b):
    if (a == 0 or b == 0):
       return 0
    
    if (a == b):
        return a
 
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


def base(val1,base1):
    l = []
    val = val1
    while (val > 0):
        rem = val % base1
        l.append(rem)
        val = val // base1
    return sum(l)


case1 = int(input())
for x in range(case1):
    val1 = int(input())
    sum1 = 0
    for y in range(2,val1):
    
        sum1 += base(val1,y)
    
    k = gcd(sum1,val1-2)
    
    if (k == 1):
        print (val1-2)
    else:
        if (val1-2-k) == 0:
            print (1)
        else:
            print (val-2-k)
    
    
