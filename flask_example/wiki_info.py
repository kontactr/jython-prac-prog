from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup


def url_carw(title: str):
    url = "https://en.wikipedia.org/wiki/"
    #url = "https://www.zomato.com/"
    
    url += str(title)

    h = {"User-Agent":""}

    request = Request(url,headers=h)
    resp =  urlopen(url)

    link_data = BeautifulSoup(resp,"html5lib")

    list_info = []


    for data in link_data.findAll("p"):
                #if(("data)): #or ("<a" in data) or ("<p" in data)  or ("<div" in data)):
                #assert isinstance(data.text, object)
                list_info.append(str(data))

    st = ""
    #list_info.remove("")
    for data in list_info:
        st+= (data)

    return st


