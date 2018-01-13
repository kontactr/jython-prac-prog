def prime(num):
    if num == 1:
        return False
    else:
        for x in range(2,int(num**0.5+1)):
            if num % x == 0:
                return False
        return True

for case1 in range(int(input())):
    val = int(input())
    if(prime(val)):
        for x in range(1,val+1):
            if not(prime(x) and prime(val-x)):
                   print (2)
                   break
    elif val == 3:
                   print (3)

    else:
        print (1)
