case1 = int(input())
for k in range(case1):
    size = int(input())
    arr = list(map(int,input().strip(" ").split(" ")))
    c_arr ,c_arr1 = 0, 0
    arr1 = arr.copy()
    for x in range(size-1):
        if arr[x] >= arr[x+1]:
            arr[x+1] = arr[x] + 1
            c_arr += 1
        else:
            pass
        if arr1[x] >= arr1[x+1]:
            if (x == 0):
                arr1[x] = arr1[x+1] - 1
            else:
                arr1[x] = (arr1[x-1] + arr1[x+1]) // 2 + 1
            c_arr1 += 1
                print (arr1,"arr1 - 1")
    print (c_arr,c_arr1)
    if c_arr < c_arr1:
        print (c_arr)
    else:
        print (c_arr1)
    
    
