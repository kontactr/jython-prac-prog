size , case1 = input().strip(" ").split(" ")
arr = sorted(list(map(int,input().strip(" ").split(" "))))
l = []
for k in range(int(case1)):
    m_s,ma_s = list(map(int,input().strip(" ").split(" ")))
    count = 0
    for item in arr:
        if item >= m_s and item<=ma_s:
            count += 1
        elif item > ma_s:
            break
    l.append(str(count))
print ("\n".join(l))
