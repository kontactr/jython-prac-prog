import urllib.request as ur
import urllib.parse as up
url = "https://www.google.com/search?"
values = {'q':"hello world program",'#':"in python"}

h = {}
h['User-Agent'] = ""
#"Safari/5.0 (X11 linux i686)"

data = up.urlencode(values)
url += data
req = ur.Request(url,headers = h)
resp = ur.urlopen(req)
for val in list(map(lambda x: x.decode("utf-8"),resp.readlines())):
    if "hello world program" in val :
        if "href" in val :
            print (val)
            print("\n\n")
print ("end")
