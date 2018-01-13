x = int(input())
for k1 in range(x):
    a = int(input())
    arr = input().strip(" ").split(" ")
    arr = list(map(int,arr))
    from collections import Counter
    arr =  sorted(arr, key=Counter(arr).get, reverse=False)
    print (arr)
    if (arr.count(arr[0]) == 1):
        print (arr[0])
    else:
        print (-1)
    
