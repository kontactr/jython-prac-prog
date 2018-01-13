from java.net import URL

url = URL("https://www.google.co.in/?gfe_rd=cr&ei=8jCkWNfYK4Pj8weB8qeABw&gws_rd=ssl")
print (url)
print ("File: "+url.getFile())
print ("path: "+url.getPath())
print ("Port: "+str(url.getPort()))
print ("Host: "+url.getHost())
print ("protocol: "+url.getProtocol())
k = url.getContent()
print("Authority: "+url.getAuthority())
print ("Querystring: "+url.getQuery())
#print ("userInfo: "+str(url.getUserInfo()))
#print ("ref: "+url.getRef())
