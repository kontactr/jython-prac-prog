di = {"a":"z",
"b":"a",
"c":"b",
"d":"c",
"e":"d",
"f":"e",
"g":"f",
"h":"g",
"i":"h",
"j":"i",
"k":"j",
"l":"k",
"m":"l",
"n":"m",
"o":"n",
"p":"o",
"q":"p",
"r":"q",
"s":"r",
"t":"s",
"u":"t",
"v":"u",
"w":"v",
"x":"w",
"y":"x",
"z":"y"}

def trans(p,q,st):
    p1= list(st)
    for x in range(p-1,q):
        p1[x] = di[p1[x]]
    return "".join(map(str,p1))

for case1 in range(int(input())):
    inp = input().split(" ")
    st = input()
    for x in range(int(inp[1])):
        ip = input().split(" ")
        st = trans(int(ip[0]),int(ip[1]),st)
    print (st)
    
        
