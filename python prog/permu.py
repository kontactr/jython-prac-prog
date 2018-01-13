for case1 in range(int(input())):
    size = int(input())
    arr1 = list(map(int,input().strip(" ").split(" ")))
    arr= arr1
    xor = 0
    for x,y in enumerate(arr):
            for l in arr[x+1:]:
                if y>l:
                    xor += 1
    
    for k in range(1,size):
        arr = arr1[k:]+arr1[:k]
        count = 0
        for l in arr[1:]:
            if arr[0]>l:
                count += 1
        print (count)
        xor ^= count
    print (xor)
