#input of state like 1 -> q1,q2,...qn
#ini and final state are currently not available
#first - total number of state and symbol_count
#and then after for each state we input symbol and its transition
#then finally convert into set and put data into the function
#write_nfa_graph by default name hello.png
#and it is stored at dir which prog displayed at first line when you
#saw the output
#python version 3.X +

import pydot as p
from PIL import Image
import os

graph = p.Dot(graph_type='digraph')
graph1 = p.Dot(graph_type='digraph')
print (os.getcwd())

def anagram(list_str_l , data):
    for key_l_s in list_str_l:
        if set(key_l_s) == set(data):
            return True
        else:
            pass
    return False

#se = None

def accepts(transitions,initial,accepting,s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting


def write_nfa_graph(ds,se_0,se_1,un):
    keys = ds.keys()
  #  print (keys)
    for key in keys:
 #       print (key)
        if key in {}:
            continue
        else:
            keys_symbol_list = ds[key].keys()
            for key_symbol in keys_symbol_list:
                if key_symbol in {}:
                    continue
                else:
                    values_symbol = ds[key][key_symbol]
                    for k in values_symbol:
                        if k in {}:
                            continue
                        else:
                      #      if k in se[1] and k in se[0]:
                       #         temp = p.Edge(key+" S F ",k)
                        #    elif k in se[0]:
                         #       temp = p.Edge(key+" S ",k)
                          #  elif k in se[1]:
                           #     temp = p.Edge(key+" F ",k)
                           # else:
                            
                            if k in un :
                                print ("key in un "+key)
                                n1 = p.Node(k, style="filled", fillcolor="yellow")
                            elif k in se_0:
                                print ("key in se_0 "+key)
                                #if key in se_0 or k in se_0:
                                n1 = p.Node(k, style="filled", fillcolor="blue")
                            elif k in se_1:
                                print ("key in se_1 "+key)
                                n1 = p.Node(k, style="filled", fillcolor="red")
                            else:
                                print ("key in else "+key)
                                n1 = p.Node(k, style="filled", fillcolor="white")
                            n2 = p.Node(key)
                            graph.add_node(n1)
                            graph.add_node(n2)
                            #C70037
                            temp = p.Edge(n2,n1)
                            temp.set_fontcolor("#C70039")
                            print (key,key_symbol,k)
                            temp.set_labeldistance("20")
			    #temp.set_label(key_symbol)
                            temp.set_label(key_symbol)
                            graph.add_edge(temp)
    graph.write_png("hello.png")

def write_fa_graph(ds_fa,se_0,se_1,un):
    #-----fa start-------#
    keys_ds_fa = ds_fa.keys()
    print (keys_ds_fa)
    for key_fa in set(keys_ds_fa):
         sub_key_fa = ds_fa[key_fa].keys()
         for sub_key_val in set(sub_key_fa):
                 n1 = p.Node(key_fa)
                 n2 = p.Node(ds_fa[key_fa][sub_key_val])
                 graph1.add_node(n1)
                 graph1.add_node(n2)
                 temp = p.Edge(n1,n2)
                 temp.set_label(sub_key_val)
                 graph1.add_edge(temp)
    graph1.write_png("nfa_fa.png")
    #-----fa end---------#'''
    

state = int(input("Enter total state number: "))
symbol = int(input("Enter total symobl number: "))

ds = {}
l = {None}
l.pop()
for s_co in range(state):
    state_name = input("Enter "+str(s_co)+" state name: ")
    ds[state_name] = {}
    
    
    for symbol_count in range(int(input("howmany symbol you want to enter: "))):
        #example a -> s1,s2,s3
        symbol_entry = input("Enter symbol and state (one to many): ").split("->")
        print (symbol_entry)
        for k in range(len(symbol_entry)):
            symbol_entry[k] = symbol_entry[k].strip()
        l.add(symbol_entry[0])
        if symbol_entry[0] in ds[state_name]:
          val1 = ds[state_name][symbol_entry[0]]
          ds[state_name][symbol_entry[0]] = val1.union(set(symbol_entry[1].split(",")))
        else:
            ds[state_name][symbol_entry[0]] = set(symbol_entry[1].split(","))


se = input("Enter ini and final state: ").split(" ")
start = se[0]
se[0] = set((se[0]).split(","))
se[1] = set((se[1]).split(","))
un = se[0].intersection(se[1])
#print (se)
#print (un)
print (l)
write_nfa_graph(ds,se[0],se[1],un)
print (ds)

l_queue = []
l_rev = []
ds_fa = {}
ds_fa[start] = {}
for k in l:
    
   ds_fa[start][str(k)] = ""
   if str(k) in ds[start]:
           
       temp_l = list(ds[start][str(k)])
       st = ""
       for ty in temp_l:
               st += ty+" "
       ds_fa[start][str(k)] = st.strip()
       l_queue.append(st.strip())
   #l_rev += start.split(",") 
#print ()   
print (l_queue)
print (ds_fa)
print("\n")

#one loop will beadded for all the start symbol which is 'for loopq in ds[start]: '
while len(l_queue) > 0:
    try:
        while l_queue[0] in {''} and len(l)>0:
            ch_pop = l_queue.pop(0)
        try:
            ch_pop = l_queue.pop(0)
            ds_fa[ch_pop] = {}
        except:
            break
    except:
        break
    if ch_pop not in l_rev:
        l_rev.append(ch_pop)
    state_list = ch_pop.split(" ")
    for sym_num in l:
        ds_fa[ch_pop][sym_num] = ""
        string = ""
        for state_eve in state_list:
            if sym_num in ds[state_eve]:
                temp_l = list(ds[state_eve][str(sym_num)])
                for cou in temp_l:
                        string += cou + " "
        string = string.strip()
        teml = list(set(string.split(" ")))
        string = ""
        for qw in teml:
            string += qw + " "
        string = string.strip()
        ds_fa[ch_pop][sym_num] = string
        if not (anagram(l_rev,string)):
            l_queue.append(string)
        else:
            pass
        print ("queue: ",l_queue)
        print ("rev: ",l_rev)

start = start.split(",")
for start_lk in start:
    if not anagram(l_rev,start_lk):
        l_rev.append(start_lk)
print ("queue: ",l_queue)
print ("rev: ",l_rev)
flag = False
for st in ds_fa.keys():
    for num_l in l:
        if ds_fa[st][num_l] == '':
            ds_fa[st][num_l] = "dead"
            flag = True
if(flag):
    ds_fa["dead"] = {}
    for dead_num in l:
        ds_fa["dead"][str(dead_num)] = "dead"

print("\n\n\nds_fa:\n\n\n")


print (ds_fa)

write_fa_graph(ds_fa,None,None,None)

#print (accepts(ds,'q0',{'q3'},'1011101'))
