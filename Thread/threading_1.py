import threading

lock = threading.Lock()

l = []

def ins():
    for y in range(1,10):
        global l
        #lock.acquire()
        l.append(input())
        #lock.release()

def dis():
    for y1 in range(1,10):
        global l
        #lock.acquire()
        print (l)
        #lock.release()

t1 = threading.Thread(target = ins,args=[])
t2 = threading.Thread(target = dis,args=[])
t1.start()
t2.start()
t1.join()
t2.join()
