import threading 

ele = input().strip(" ").split(" ")
val_find = input().strip(" ")
lock = threading.Lock()
flag = True

def check(li,val):
    global flag
    for x in li:
        lock.acquire()
        if flag:
            if val == x:
                print ("YES" , threading.current_thread().getName())
                flag = False
        lock.release()
        if(not flag):
            break

t1 = threading.Thread(target=check , args=[ele[:len(ele)//2],val_find])
t2 = threading.Thread(target=check , args=[ele[len(ele)//2:],val_find])
t1.start()
t2.start()

t1.join()
t2.join()

if(flag):
    print ("Not Found", threading.current_thread().getName())
        
