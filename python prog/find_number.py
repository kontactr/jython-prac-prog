def bs(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bs(arr, l, mid-1, x)
        else:
            return bs(arr, mid+1, r, x)
    else:
        return -1


size , find = list(map(int,input().strip(" ").split(" ")))
arr = list(map(int,input().strip(" ").split(" ")))
l = []
for k in range(len(arr)-1):
    for j in range(k+1,len(arr)):
        l.append(abs(arr[k] - arr[j]))
l.sort()
print (bs(l,0,len(arr),find))
