for lq in range(int(input())):
    guests = int(input())
    room = [ [-1]  for i in range(guests) ]

    di = {arr:stay for arr,stay in zip(list(map(int,input().strip(" ").split(" "))),list(map(int,input().strip(" ").split(" "))))}
    di[-1] = -1

    keys = list(di.keys())
    keys.remove(-1)

    for arr in keys:
        for count_room in room:
            if (di[count_room[-1]] + count_room[-1] -1) < arr:
                count_room[0] = arr
                break

    room.append([-1])

    print (room.index([-1]))
