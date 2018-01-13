a = input()
arr = list(input())
if int(a) < 4:
    print (0)
else:
    count = 0 
    for j in range(0,len(arr)-3):
        for j1 in range(j+1,len(arr)-2):
            for j2 in range(j1+1,len(arr)-1):
                for j3 in range(j2+1,len(arr)):
                    if arr[j] == arr[j2] and arr[j1] == arr[j2]:
                        count += 1
    print (count)
      
