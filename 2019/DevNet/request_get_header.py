#__author:"Peter"
#date:2019/12/4
import requests
r = requests.get('http://124.42.239.81:1689/ygnetERP/a/login')

#获取头部内容
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers.get('Content-Type'))

#获取Cookie(Cookie为头部内容)
print(r.cookies.get_dict())
print(r.cookies.keys())
print(r.cookies.get('jeesite.session.id'))
#print(r.cookies.get('csrftoken'))