for k in range(int(input())):
    di = {}
    st = input()
    for p in st:
        if p not in di:
            di[p] = 1
        else:
            pass
    print ("".join(list(di.keys())))
