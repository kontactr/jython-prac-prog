n , m = list(map(int , input().strip(" ").split(" ")))
graph = []
start , end = () , ()
distance = []
visited = set()

##BACK PRAPOGATION REMAINING
##RECURSION PATH FINDING
##ONLY FOLLOWS TILL H
##START POINT V
##END POINT H
##3 3
##V..
##...
##..H
##(0, 0) (2, 2)  0
##Front - 1 
##(1, 0) (2, 2) FRONT 0
##(2, 0) (2, 2) FRONT 0
##(2, 1) (2, 2) RIGHT 1
##(1, 1) (2, 2) RIGHT 1
##(1, 2) (2, 2) RIGHT 1
##RIGHT - 1 
##(0, 1) (2, 2) RIGHT 0
##(0, 2) (2, 2) RIGHT 0
##>>> distance
##[1, 1, 0]

for k in range(n):
    row = list(input())
    if 'V' in row:
       start = (k,row.index('V'))
    if 'H' in row:
        end = (k,row.index('H'))
    graph.append(row)

def recur(graph , start , end , count , direction="" , visited=set()):
    print (start , end , direction , count , visited)
    if (start[1] == 0):
        if (start[0] == 0):
            flag = False
            if (direction == ""):
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    print ("Front - 1 ")
                    recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , set())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited): 
                    visited.add((start[0] , start[1]+1))
                    print ("RIGHT - 1 ")
                    recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT" , set())
                    flag = True
                    
            else:
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    if (direction == "FRONT"):
                        print ("Front - 2 ")
                        recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , visited.copy())
                    else:
                        print ("Front - 3 ")
                        recur (graph , (start[0]+1 , start[1]) , end , count+1 ,"FRONT", visited.copy())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                    visited.add((start[0] , start[1]+1))
                    
                    if (direction == "RIGHT"):
                        print ("RIGHT - 2 ")
                        recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT", visited.copy())
                    else:
                        print ("RIGHT - 3 ")
                        recur (graph , (start[0] , start[1]+1) , end , count+1 ,"RIGHT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)
                
        elif (start[0] == n-1):
            flag = False
            if (direction == ""):
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                    visited.add((start[0] , start[1]+1))
                    recur (graph , (start[0] , start[1]+1) , end , count ,"LEFT" , set())    
                    flag = True
                    
            else:
                
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                    visited.add((start[0] , start[1]+1))
                    
                    if (direction == "RIGHT"):
                        recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT", visited.copy())
                    else:
                        
                        recur (graph , (start[0] , start[1]+1) , end , count+1 ,"RIGHT", visited.copy())
                    flag = True    
                    
            if(not flag):
                distance.append(count)
        else:
            flag = False
            if (direction == ""):
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , set())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited): 
                    visited.add((start[0] , start[1]+1))
                    recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT" , set())
                    flag = True
                    
            else:
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    if (direction == "FRONT"):
                        recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , visited.copy())
                    else:
                        recur (graph , (start[0]+1 , start[1]) , end , count+1 ,"FRONT", visited.copy())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                    visited.add((start[0] , start[1]+1))
                    
                    if (direction == "RIGHT"):
                        recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]+1) , end , count+1 ,"RIGHT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)
            
    elif (start[1] == m-1):
        if (start[0] == 0):
            flag = False
            if (direction == ""):
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , set())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited): 
                    visited.add((start[0] , start[1]-1))
                    recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT" , set())
                    flag = True
                    
            else:
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    if (direction == "FRONT"):
                        recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT", visited.copy())
                    else:
                        recur (graph , (start[0]+1 , start[1]) , end , count+1 ,"FRONT", visited.copy())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited):
                    visited.add((start[0] , start[1]-1))
                    if (direction == "RIGHT"):
                        recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]-1) , end , count+1 ,"LEFT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)
            
        elif (start[0] == n-1):
            flag = False
            if (direction == ""):
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited): 
                    visited.add((start[0] , start[1]-1))
                    recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT" , set())
                    flag = True
                    
            else:
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited):
                    visited.add((start[0] , start[1]-1))
                    if (direction == "LEFT"):
                        recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]-1) , end , count+1 ,"LEFT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)

        else:
            flag = False
            if (direction == ""):
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , set())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited): 
                    visited.add((start[0] , start[1]-1))
                    recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT" , set())
                    flag = True
                    
            else:
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    if (direction == "FRONT"):
                        recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT", visited.copy())
                    else:
                        recur (graph , (start[0]+1 , start[1]) , end , count+1 ,"FRONT", visited.copy())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited):
                    visited.add((start[0] , start[1]-1))
                    if (direction == "LEFT"):
                        recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]-1) , end , count+1 ,"LEFT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)
    else:
            flag = False
            if (direction == ""):
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT" , set())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited): 
                    visited.add((start[0] , start[1]-1))
                    recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT" , set())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                        visited.add((start[0] , start[1]+1))
                        recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT" , set())
                        flag = True
                        
            else:
                if(start[0]+1 < n and graph[start[0]+1][start[1]] == "." and (start[0]+1 , start[1]) not in visited):
                    visited.add((start[0]+1 , start[1]))
                    if (direction == "FRONT"):
                        recur (graph , (start[0]+1 , start[1]) , end , count ,"FRONT", visited.copy())
                    else:
                        recur (graph , (start[0]+1 , start[1]) , end , count+1 ,"FRONT", visited.copy())
                    flag = True
                    
                if (start[1]-1 > -1 and graph[start[0]][start[1]-1] == "." and (start[0] , start[1]-1) not in visited):
                    visited.add((start[0] , start[1]-1))
                    if (direction == "LEFT"):
                        recur (graph , (start[0] , start[1]-1) , end , count ,"LEFT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]-1) , end , count+1 ,"LEFT", visited.copy())
                    flag = True
                    
                if (start[1]+1 < m and graph[start[0]][start[1]+1] == "." and (start[0] , start[1]+1) not in visited):
                    visited.add((start[0] , start[1]+1))
                    if (direction == "RIGHT"):
                        recur (graph , (start[0] , start[1]+1) , end , count ,"RIGHT", visited.copy())
                    else:
                        recur (graph , (start[0] , start[1]+1) , end , count+1 ,"RIGHT", visited.copy())
                    flag = True
                    
            if(not flag):
                distance.append(count)

recur(graph,start,end,0,"" , visited)


