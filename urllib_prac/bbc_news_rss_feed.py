from bs4 import BeautifulSoup as bs
import urllib.request as ur

url = "http://feeds.bbci.co.uk/news/world/rss.xml"
h = {"User-Agent":""}

req = ur.Request(url,headers=h)
resp = ur.urlopen(req)

xml = bs(resp,"xml")


for link in xml.findAll("link"):

    req1 = ur.Request(link.text,headers=h)
    resp1 = ur.urlopen(req1)
    xml1 = bs(resp1,"html5lib")

    for news in xml1.findAll("p"):

        print (news.text)


print ("end")
    

