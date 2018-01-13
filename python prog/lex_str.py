a , b = input().strip(" ").split(" ")
print ("".join((sorted([ sorted(list(a[k:]))  for k in range(len(a)) ])[int(b)-1])))
