def answer(total_lambs):
    print (abs(len(stingy([1,1],total_lambs))  - len(generous([1],total_lambs))))


def stingy(list_of_emp,total_lambs):
    total = total_lambs
    total -= (list_of_emp[-2] + list_of_emp[-1])
    while (list_of_emp[-1] + list_of_emp[-2]) <= total :
        list_of_emp.append(list_of_emp[-1] + list_of_emp[-2] )
        total -= list_of_emp[-1]
    print ((list_of_emp), "stingy")
    return list_of_emp


def generous(list_of_emp,total_lambs):
    total = total_lambs
    total -= list_of_emp[-1]
    while list_of_emp[-1] * 2 <= total :
        list_of_emp.append(list_of_emp[-1] * 2 )
        total -= list_of_emp[-1]
    print ((list_of_emp), " ")
    return list_of_emp


answer(731)
    
