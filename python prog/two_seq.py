st = list(input())
size = len(st)
if size == 1:
    st[0] = 'a'
else:
    if st[0] == '?':
        if st[1] == 'a':
            st[0] = 'b'
        else:
            st[0] = 'a'
for k in range(1,size-1):
    if st[k] == '?':
        if ((st[k-1] != 'a') and (st[k+1] != 'a')):
            st[k] = 'a'
        else:
            st[k] = 'b'
else:
    if st[-1] == '?':
        if st[-2] == 'a':
            st[-1] = 'b'
        else:
            st[-1] = 'a'
print (st)
    
