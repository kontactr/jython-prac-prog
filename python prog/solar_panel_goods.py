def answer(area):
    calc = area
    lar_squ_list = []
    while (calc != 0):
        temp = int((calc ** 0.5) // 1)
        lar_squ_list.append(temp ** 2)
        calc = calc - lar_squ_list[-1]
    return lar_squ_list

print (answer(15324)) 
