from bs4 import BeautifulSoup as bs
import urllib.request as ur

req = ur.Request("https://news.google.com/?output=rss",headers=
                 {"User-Agent":""})

resp = ur.urlopen(req)

xml = bs(resp,"xml",exclude_encodings="utf-8")

for item in xml.findAll("link"):
    try:
        print (item.text)
        req1 = ur.Request(item.text,headers={"User-Agent":""})
        news = ur.urlopen(req1)
        page = bs(news,"html5lib")


        for n in page.findAll("p"):
            print (n.text)
    except Exception as e:
        print (e)

print("end")
