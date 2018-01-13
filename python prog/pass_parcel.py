a = list(range(1,int(input())+1))
song = input()
ball = 0
while (len(a) != 1):
    for k in song:
        if(len(a) != 1):
             
             if k == 'a':
                if (ball == len(a)-1):
                     ball = 0
                else:
                     ball += 1
             else:
                 if (ball == len(a)-1):
                     a.pop(ball)
                     ball = 0
                 else:
                     a.pop(ball)   
print (a[0])
         
         
