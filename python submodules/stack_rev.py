def reverse(stack):
    start = 0
    end = len(stack) - 1
    
    def recur(stack , start , end):
        if start > end:
            return
        else:
            temp = stack[start]
            stack[start] = stack[end]
            stack[end] = temp
            recur(stack, start+1 , end-1)

    recur(stack , 0 ,len(stack) - 1)

    print (stack)



def tower_of_hanoi(number , start , middle , end , result=[]):
    if number < 2:
        result.append("disk "+" from "+str(start)+" to "+str(end))
    else:
        tower_of_hanoi(number-1 , start , end, middle , result)
        tower_of_hanoi(1 , start , middle , end , result)
        tower_of_hanoi(number-1 , middle , start , end, result)
        return result


def bubble(stack):
    start = 0
    end = len(stack) - 1

    def recur(stack , start , end):
        if(start == end):
            return
        else:
            if stack[start] > stack[end]:
                temp = stack[start]
                stack[start] = stack[end]
                stack[end] = temp            
            recur(stack , start+1 , end)
            recur(stack , start , end - 1)

    recur(stack , start , end)


def length(string):
    original = (string + "\0")

    def recur(string):
        if string[0]:
            try:
                if string[1]:
                    return 1 +recur(string[1:])
            except:
                return 1
    return recur(original) - 1


def sum_of_digit(number):
    if int(number) > 0:
        return number%10 + sum_of_digit(number // 10)
    else:
        return number


def prime(number):

    def recur(number , start , result):
        if start == result:
            return True
        else:
            return (number%start!=0) and recur(number , start+1 , result)    
    
    if number > 2 :
        return recur(number , 2 , int(number**1/2)+1)
    else:
        return True and number > 0
    

def binary_tree(tree , root):

    result = []
    def recur(tree , node , result=[]):
        if node in tree:
            val = tree[node]
            recur(tree ,tree[node][0],result)
            result.append(node)
            recur(tree ,tree[node][1],result)    
        else:
            result.append(node)
    recur(tree , root , result)
    return result


def count_occ(stack , number , index=0):
    if index == len(stack):
        return 0
    else:
        if(stack[index] == number):
            return 1 + count_occ(stack,number,index+1)
        else:
            return 0 + count_occ(stack,number,index+1)
    

def reverse_number(number,answer=0):
    if number < 1:
        return answer
    
    answer = (answer*10 + number % 10)
    return reverse_number(number // 10 , answer)
    
    
def binary_tree_dict(dicti):
    result = []
    def recur(dicti,index,keys,result):
        print (dicti , index, keys , result)
        if index == len(keys):
            return
        else:
            if  dicti[keys[index]] == None:
                result.append(keys[index])
            else:
                result.append(keys[index])    
                recur(dicti[keys[index]] , 0 , list(dicti[keys[index]].keys()) , result)
            
            recur(dicti , index+1 , keys, result)
            
        
    recur(dicti , 0 , list(dicti.keys()) , result)
    return result
    
    

def copy_string(string):
    if len(string) == 1:
        return string
    else:
        return string[0] + copy_string(string[1:])

def pail(string):

    def recur(string,start , end):
        print (start , end)
        if start >= end:
            return True
        if(string[start] == string[end]):
            print (start , end)
            return True and recur(string,start+1,end-1)
        else:
            return False

    return recur(string , 0 , len(string)-1)

def pail_string(string):
    if(len(string) == 1):
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        return string[0] == string[-1] and pail_string(string[1:-1])


def single_list(list_data,result=[],index=0):
    
    print (index , list_data , result)
    if index == len(list_data):
        return
    if type(list_data[index]) == type([]):
        single_list(list_data[index] , result , 0)
    else:
        result.append(list_data[index])
    single_list(list_data , result , index+1)


def single_json(json):
    result = []
    def recur(element , keys , data_type , index , result):
        print (element , keys , data_type , index , result , )
        if (data_type == type({})):
            if len(keys) <= index:
                return
            
            
            if type(element[keys[index]]) == type({}):
                recur(element[keys[index]] ,list(element[keys[index]].keys()) , type({}) , 0 , result) 

            elif type(element[keys[index]]) == type([]):
                recur(element[keys[index]] , element[keys[index]] , type([]) , 0 , result)

            else:
                
                result.append(element[keys[index]])
            recur(element , keys , type({}) , index + 1 , result)

        elif (data_type == type([])):
            if len(keys) <= index:
                return

            if type(element[index]) == type({}):
                recur(element[index] , list(keys[index].keys()) , type({}) , 0 ,result)

            elif type(element[index]) == type([]):
                recur(element[index] , keys[index] , type([]) ,0 , result)

            else:
                result.append(keys[index])
            recur(element , keys , type([]) , index+1 , result)

        else:
            result.append(element)
        
    recur(json , list(json.keys()) , type(json) , 0 , result)
    return result

def double_loop(array):
    result = []
    def recur(array, row , column , length , result):
        if column >= length:
            if row < length-1:
                recur(array , row+1 , 0 , length , result)
            else:
                return
        else:
            result.append(str(row)+" "+str(column))
            recur(array , row , column+1 , length , result)

    recur(array , 0 , 0, len(array) , result)
    return result
        
    
        
def main_test():      
    l = [1,2,3,4,5]
    reverse(l)
    print (l)

    l = [5,4,3,2,1 , 6 , -1, -2, -3, 9, 10]
    bubble(l)
    print (l)

    print (tower_of_hanoi(3,"A","B","C"))

    print (length("Aaaaa\0\0\0\0"))

    print (sum_of_digit(101010))

    print(prime(10))

    print (binary_tree({1:[2,3] , 2:[4,5] , 3:[6,7]} , 1))

    print (count_occ([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] , 1))


    print (binary_tree_dict({1: {2: None , 10:{11:{12:None,13:None}}}, 3: {4: {5: None , 6:{7:None , 8:{9:None}}}}}))

    print (reverse_number(123))

    print (copy_string("abcd"))

    print (pail("aba"))

    print (pail("abba"))

    print (pail_string("aba"))

    print (pail_string("abba"))

    li = [1,2,3,4,5,[6,7],8,9,10,[11,[12,[34,35],36],37],[[[[[]]]],39]]
    result = []
    print (single_list(li , result , 0),result)

    print (single_json({1:1,2:2,3:[4,5,{},[{9:{9:[{},{},[],{}]}},{},[90]]],6:{7:8,9:10,11:12}}))

    print (double_loop([1,2,3,4,5,6]))

if __name__ == "__main__":
    main_test()
