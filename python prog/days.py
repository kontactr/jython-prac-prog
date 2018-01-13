case1 = int(input())
d = {1:"MONDAY",2:"TUESDAY",3:"WEDNESDAY",4:"THURSDAY",5:"FRIDAY",6:"SATURDAY",0:"SUNDAY"}
for k in range(case1):
    topic = int(input())
    days = list(map(int,input().split(" ")))
    sum1 = topic
    if topic % sum(days) != 0:
        sum1 = topic % sum(days)
    dd = 0
    l1 = 0
    while (sum1 != 0):
                if days[l1] >= 1:
                    sum1 -= days[l1]
                    dd = l1
                l1 += 1
                l1 = l1%7
    print (d[(dd+1)%7])
    
            
    
