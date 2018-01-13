import _thread as thread
import random

a = []

def check_odd(a):
    while(len(a)%2 != 50):
        if (len(a)%2):
            print ("ODDD" , a)

def check_even(a):
    while (len(a) != 50):
        if not(len(a)%2):
            print ("EVEN" , a)


try:
    thread.start_new_thread(check_odd,(a,))
    thread.start_new_thread(check_even,(a,))
except Exception as e:
    print (e)

while thread._count() == 1:
    print (thread._count())

while (len(a) != 50):
    print (thread._count())
    a.append(random.randint(10,20))

c = input()


    
        
