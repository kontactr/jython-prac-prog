for case1 in range(int(input())):
    size , k = input().strip(" ").split(" ")
    k = int(k)
    l1 = k
    arr , qu = list(map(int,input().strip(" ").split(" "))), []
    while (k):
        temp = l1
        if(l1):
            for k1 in range(len(arr) - 1):
                if arr[k1] < arr[k1+1]:
                    if (l1):
                        qu.append(arr[k1])
                        l1 -= 1
                        
                    else:
                        break
            for p in qu:
                arr.remove(p)
            qu.clear()
        if temp != l1:
            k -= 11
        else:
            k -= 1
    print (" ".join(list(map(str,arr))))
        
