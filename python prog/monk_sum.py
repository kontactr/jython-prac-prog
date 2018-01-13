n , x = list(map(int,input().strip(" ").split(" ")))
arr = list(map(int,input().strip(" ").split(" ")))
arr.sort()
count = 0
if (arr[-1] <= x):
    count += 1
for k in range(2,n+1):
    if sum(arr[:-k-1:-1]) <= x:
        count += 1 
print (count)
        
