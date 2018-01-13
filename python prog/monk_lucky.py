a = int(input())
for x in range(a):
    size = input()
    arr = input().split(" ")
    if (arr.count(min(arr))) % 2 != 0:
        print ("Lucky")
    else:
        print ("Unlucky")
