size = input()
li = input().strip(" ").split(" ")
max_block = 0
temp = 0
flag = li[0]
for j in li[1:]:
    if (j=='0' and flag=='0'):
        max_block += 1
        print (max_block , j)
    elif (j=='1' and flag=='0'):
        if temp < max_block:
            temp = max_block
        max_block = 1
        print (max_block , j)
        flag = '1'
    elif (j=='1' and flag=='1'):
        max_block += 1
        print (max_block , j)
    elif (j=='0' and flag=='1'):
        if temp < max_block:
            temp = max_block
        max_block = 1
        print (max_block , j)
        flag = '0'
else:
    if temp < max_block:
        temp = max_block
print (temp)
