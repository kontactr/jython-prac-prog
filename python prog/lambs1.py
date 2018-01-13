from math import sqrt
from math import log
from math import pow

def answer(total_lambs):
    phi = (1+sqrt(5))/2  
    tau = (1-sqrt(5))/2  
    eps = pow(10, -10)

    max_hunchmen = int(round(log((total_lambs + 1) * sqrt(5)+eps, phi))) - 2
    Fib_num = int(round((pow(phi, max_hunchmen+2)-pow(tau,max_hunchmen+2))/sqrt(5)))
    if total_lambs+1 < Fib_num:
      max_hunchmen -= 1
    elif total_lambs + 1 == Fib_num:
        total_lambs = Fib_num
    if (total_lambs + 1) % 2 == 0:
         min_hunchmen = int(round(log((total_lambs + 1), 2)))
         print (min_hunchmen)
    else:
        min_hunchmen = int(log((total_lambs + 1), 2))
    print (max_hunchmen,min_hunchmen)
    return abs(max_hunchmen - min_hunchmen)


print (answer(731))
