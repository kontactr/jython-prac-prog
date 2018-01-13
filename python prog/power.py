a = int(input())
arr = sorted(list(map(int,input().strip(" ").split(" "))))
for k in range(int(input())):
    power = int(input())
    start = 0
    end = len(arr) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] == power):
            break
        elif (arr[mid] < power):
            start = mid + 1
        elif (arr[mid] > power):
            end = mid - 1
    print (mid+1 , sum(arr[:mid+1]))
