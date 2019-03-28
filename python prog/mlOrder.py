def fun1(string):
    length = len(string)
    max_lex = length
    di = {}
    counter = 0
    
    if(not length):
        return max_lex
    
    def fun2(key_index,compare_index , count, start_point):
        
        nonlocal max_lex , counter
        counter = counter + 1
        if(compare_index >= length or key_index > length):
            
            temp = (count  )

            
            if start_point in di:
                di[start_point] = min(di[start_point],temp)
            else:
                di[start_point] = temp
            
            if (max_lex >=   di[start_point]):
                max_lex = di[start_point]
            return
        elif(count > max_lex or start_point > max_lex):
            return
        else:
            

                if(string[key_index] <= string[compare_index]):
                    if compare_index in di:
                        value = di[compare_index] - compare_index
                        newValueForAdd = value + count 

                        if start_point in di:
                            di[start_point] = min(di[start_point] , newValueForAdd)
                        else:
                            di[start_point] = newValueForAdd

                        if (max_lex >= di[start_point]):
                            max_lex = di[start_point]
                    
                        fun2(key_index, compare_index + 1 , count + 1,start_point)
                    else:
                        fun2(compare_index , compare_index + 1 , count,start_point)
                        fun2(key_index, compare_index + 1 , count + 1,start_point)
                else:
                        fun2(key_index, compare_index + 1 , count + 1,start_point)
                fun2(key_index+1 , key_index + 2 , key_index+1,key_index+1)
            
    fun2(0,1,0,0)
    print (di,counter)
    return {"max_lex_delete": max_lex,
            "max_lex_present": length - max_lex,
            "max_iteration": counter
            }



def test():
    print (fun1("avcdefghija")["max_lex_delete"] == 2)
    print (fun1("banana")["max_lex_delete"] == 3)
    print (fun1("baae")["max_lex_delete"] == 1)
    print (fun1("cvbcvbcvb")["max_lex_delete"] == 5)
    pass


if __name__ == "__main__":
    test()
print(fun1(input()))
