from bs4 import BeautifulSoup
from urllib.request import Request as R ,urlopen as uo

url = "http://synd.cricbuzz.com/j2me/1.0/livematches.xml"
h = {'User-Agent' : ''}

req = R(url,headers=h)
resp = uo(req)

xml = BeautifulSoup(resp,"xml")

for val in xml.find("mchdata"):
    print (val)


