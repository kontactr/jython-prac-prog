for case1 in range(int(input())):
    date = input().strip(" ").split("-")
    if (set(date[0]).union(set(date[1])) == set(date[2])):
        print ("Lucky Watson")
    else:
        print ("Unlucky Watson")
