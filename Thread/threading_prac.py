from threading import Thread
import sys

def op(sd):
    oper = sd.readline().strip("\n")
    print (oper)
    for x in open("input.txt"):
        if oper in x:
            print (x)

p = Thread(target=op, args=[sys.stdin])
p.start()

p.join()
