for case1 in range(int(input())):
    size,rot = list(map(int,input().split(" ")))
    arr = input().split(" ")
    rot = rot % size
    if (rot == 0):
        print (" ".join(arr))
    else:
        print (" ".join(arr[-rot:]+arr[:-rot]))
