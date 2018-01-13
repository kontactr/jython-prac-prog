def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

for case1 in range(int(input())):
    try:
        val = list(map(int,input().split(" ")))
        sum1 = ((val[0]//val[1])*(val[1]+ (val[0]//val[1])*val[1])) / 2
        sum2 = ((val[0]//val[2])*(val[2]+ (val[0]//val[2])*val[2])) / 2
        g = 1
        if case1 == 0:
            g = lcm(val[1],val[2])
        else:
            g = val[1]*val[2]
        sum3 = ((val[0]//(g))*((g)+ (val[0]//(g))*(g))) / 2
        print (int(sum1+sum2 - sum3))
    except Exception as e:
        print (0)
