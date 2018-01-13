di = {}
for k in range(97,123):
    di[chr(k)] = k-96
print (di)

for case1 in range(int(input())):
    a  = input()
    if a == a[::-1]:
        print ("Palindrome")
    else:
        mul = 1
        for k1 in a:
             mul *= di[k1]
             print (k1,di[k1])
        print (mul)
