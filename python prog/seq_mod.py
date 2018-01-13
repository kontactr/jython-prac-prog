a = input()
arr = list(map(int,input().split(" ")))
print (arr)
if(len(arr) == 1):
    print ("YES")
elif (len(arr) == 2):
    if (arr[0] == arr[1]):
        print ("YES")
    else:
        print("NO")
else:
    temp =arr[1]
    if (arr[1:-1].count(temp) == len(arr[1:-1])) and ((arr[0]+1 == arr[1]) and (arr[-1]+1 == arr[-2])):
        print ((arr[0]+1 == arr[1]))
        print ((arr[-1]+1 == arr[-2]))
        print ("YES")
    else:
        print ("NO")
