s = input()
box = list(map(int,input().strip(" ").split(" ")))
max_area = 0
for k in range(len(box)):
    for j in range(k,len(box)):
        temp = box[k:j+1]
        temp = len(temp) * min(temp)
        if max_area < temp:
            max_area = temp
print (max_area)
