import _thread as thread

lock = thread.allocate_lock()

class a1():
    def __init__(self):
        self.i = 0

def incre(a):
    #while a.i < 10:
        q = 0
        while q < 10:
            q += 1
        lock.acquire()
        print (a.i , "INC")
        a.i += 1
        lock.release()
        print (thread._count())

def decre(a):
    #while a.i < 10:
        q = 0
        while q < 10:
            q -= 1
        lock.acquire()
        print (a.i , "DEC")
        a.i -= 1
        lock.release()

obj = a1()
thread.start_new_thread(incre,(obj,))
thread.start_new_thread(decre,(obj,))

while thread._count() == 1:
    pass

while thread._count() != 1:
    print (thread._count())
