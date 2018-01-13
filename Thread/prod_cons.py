import threading

lock = threading.Lock()

class item:
    def __init__(self):
        self.product = 0


class producer(threading.Thread):
    def __init__(self,item):
        threading.Thread.__init__(self)
        self.item = item

    def run(self):
        while True:
            if self.item.product < 10:  
                self.item.product += 1
                print (self.item.product,threading.currentThread().getName())
            else:
                notify()
                wait()
            

class consumer(threading.Thread):
    def __init__(self,item):
        threading.Thread.__init__(self)
        self.item = item

    def run(self):
            #lock.acquire()
        while True:
            if self.item.product > 10:  
                self.item.product -= 1
                print (self.item.product,threading.currentThread().getName())
            else:
                notify()
                wait()
            #lock.release()



i1 = item()
p1 = producer(i1)
c1 = consumer(i1)

p1.start()
c1.start()


p1.join()
c1.join()
