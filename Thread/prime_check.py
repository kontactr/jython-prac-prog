import threading
from datetime import datetime as da

lock = threading.Lock()

flag = True

def check_prime(val,start,end):
    for j in range(start,end+1):
        lock.acquire()
        global flag
        if flag:
            if val%j == 0:
                print (j)
                print ("NOT PRIME" , threading.currentThread().getName())
                flag = False
        lock.release()
        if not(flag):
            break
        
val = int(input())
limit = int(val**0.5)+1
print (da.now())
t1 = threading.Thread(target=check_prime, args=(val,2,limit//2,))
t2 = threading.Thread(target=check_prime, args=(val,limit//2,limit,))
t1.start()
t2.start()
t1.join()
t2.join()
if flag:
    print ("PRIME")
print(da.now())

    
            
            
