import requests
import urllib

from flask import json

url = "http://localhost:5000/"
#data = {"username":"user_name","password":"user_password"}
#response = requests.get(url,headers={'User-Agent':'Windows'})
p = json.dumps({"A":1,"B":2})



r = requests.post(url,json=p)

print (r.json())

