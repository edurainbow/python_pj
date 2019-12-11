#__author:"Peter"
#date:2019/12/4
import requests
from requests.auth import HTTPBasicAuth
r1 = requests.get('http://192.168.63.3/level/15/exec/-/show/ip/interface/brief/CR',
                 auth=HTTPBasicAuth('admin','Cisc0123'))
r2 = requests.get('http://192.168.63.3/level/15/exec/-/show/run/CR',
                 auth=HTTPBasicAuth('admin','Cisc0123'))
print(r1.text,r2.text)