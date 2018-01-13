for case1 in range(int(input())):
    size,hour = input().split(" ")
    arr  = input().strip(" ").split(" ")
    for y in range(int(hour)):
        l = arr.copy()
        for x in range(len(arr)):
            if x>0 and x<len(arr)-1:
                if arr[x-1] == "1" and arr[x+1] == "1":
                    l[x] = "1"
                else:
                    l[x] = "0"
            elif x == 0:
                if arr[x+1] == "1":
                    l[x] = "1"
                else:
                    l[x] = "0"
            else:
                if arr[x-1] == "1":
                    l[x] = "1"
                else:
                    l[x] = "0"
        arr = l
    print(" ".join(arr))
            
