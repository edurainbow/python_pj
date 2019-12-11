#__author:"Peter"
#date:2019/12/4
import requests
headers={
    #'Host':'www.bind.com',
    'Host':'127.0.0.1:6666',
    #'User-Agent":'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/78.0.3904.97
    'User-Agent':'Mozilla/5.0(iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/534.46(KHTML,like Gecko) Chrome',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'Zh-CN,zh;q=0.9'}

r=requests.get('http://127.0.0.1:6868',headers=headers)
print(r.text)