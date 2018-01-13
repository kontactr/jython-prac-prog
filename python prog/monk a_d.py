for case1 in range(int(input())):
    val = int(input())
    arr = list(map(int,input().strip(" ").split(" ")))
    di = {}
    for ele in arr:
        k = bin(ele).count("1")
        if k in di:
            di[k] = di[k] + " " + str(ele)
        else:
            di[k] = str(ele)
    for key in sorted(di):
        print (di[key],end=" ")
