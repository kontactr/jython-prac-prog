size = input()
arr = set(input().strip(" ").split(" "))
count = 0
for x in range(int(input())):
    val = set(input().strip(" ").split(" "))
    if(arr.issubset(val)):
        count += 1
print (count)
