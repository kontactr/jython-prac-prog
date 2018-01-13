def generateRandomNumbers(size):
    range1 = 1000000007
    multiplierOne = 2017
    multiplierSecond = 2027
    lastNumber = 0
    secondLastNumber = 1
    maxNumberGeneratedTillNow = 0
    l = []
    for I in range(1,size+1):
        newNumber = (lastNumber * multiplierOne + secondLastNumber * multiplierSecond + maxNumberGeneratedTillNow) % range1 + 1
        secondLastNumber = lastNumber
        lastNumber = newNumber
        maxNumberGeneratedTillNow = max(maxNumberGeneratedTillNow,newNumber)
        l.append(newNumber)
        l.sort()
    return l

val = input().split(" ")
l = generateRandomNumbers(int(val[0]))
for ran in range(int(val[1])):
    if int(input()) in l:
        print ("YES")
    else:
        print ("NO")
