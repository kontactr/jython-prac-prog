di = {}
part = set()
visited = set()
a = int(input())
for x in range(2**a - 1):
    val = input().split(" ")
    if val[0] not in di:
        di[val[0]] = val[1]
        visited.add(val[1])
    else:
        di[val[0]] = di[val[0]] + " " + val[1]
    visited.add(val[1])
    part.add(val[0])
print (" ".join(list(part - visited)))
