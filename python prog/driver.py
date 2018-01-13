for k_case1 in range(int(input())):
    size = input()
    arr = list(map(int,input().strip(" ").split(" ")))
    l = []
    for x in range(len(arr)):
        sum1 = 0
        for j in range(x-1,0,-1):
            if arr[j] < arr[x]:
                sum1 += 1
            else:
                break
        for j1 in range(x+1,len(arr)):
            if arr[j1] < arr[x]:
                sum1 += 1
            else:
                break
        l.append((x+1)*sum1)
    print (l.index(max(l))+1)
            
