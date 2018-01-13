for case1 in range(int(input())):
    count = 0
    val = int(input())
    for v in range(1,val+1):
        for j in range(v+1,val+1):
            if v ^ j <= val:
                count+=1
    print (count)
