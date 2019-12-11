#__author:"Peter"
#date:2019/12/4
import requests
#主动抛出异常，然后用except捕获
try:
    r = requests.get('http://127.0.0.1:6868/test')
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
#产生超时异常，捕获并且打印信息
try:
    r = requests.get('http://google.com',timeout=0.001)
except requests.exceptions.ReadTimeout:
    print('读取超时')
except requests.exceptions.ConnectTimeout:
    print('连接超时')