from math import log
case1 = int(input())
for x in range(case1):
    stone,days,sto=int(input()),0,0
    if(stone == 0):
      print(sto)
      continue;
    while (stone != 0):
        
        sto =  2 ** int(log(stone,2))
        days+= 1
        stone = stone - sto
        if(stone == 1):
            days+=1
            break
    print(days)
